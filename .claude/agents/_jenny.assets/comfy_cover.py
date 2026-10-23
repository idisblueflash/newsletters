#!/usr/bin/env python3
"""Cover pipeline for _jenny: drives a local ComfyUI server through three steps.

The graphs below are API-format rebuilds of the three UI workflows in ./workflows/
(same models, LoRA, sampler settings and wiring). The Pixaroma pad/stitch nodes keep
their settings in hidden UI state, so padding and stitching happen here in Pillow.

  txt2img   Z-Image Turbo, 1024x1024                       (step01-zimage-txt2img.json)
  outpaint  Flux 2 Klein 4B + pixaoutpaint LoRA, 1440x720  (step02-Flux 2 Klein 4B Outpaint.json)
  style     Flux 2 Klein 4B, content + style reference     (step03-... Two Images Style transfer.json)

Each subcommand queues N variations with random seeds and writes them to --out,
printing one saved path per line.
"""
import argparse
import json
import random
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

SERVER = "http://localhost:8188"
WIDE_W, WIDE_H = 1440, 720
PAD_GRAY = (128, 128, 128)  # #808080, the colour the pixaoutpaint LoRA expects
OUTPAINT_PROMPT = "pixaoutpaint, replace the solid gray area by naturally extending the surrounding scene"


# The local server must never go through HTTP(S)_PROXY (a system proxy answers 502 for localhost).
_OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def _req(path, data=None, headers=None):
    req = urllib.request.Request(SERVER + path, data=data, headers=headers or {})
    try:
        r = _OPENER.open(req, timeout=60)
    except urllib.error.HTTPError as e:
        sys.exit(f"ComfyUI {path} answered {e.code}: {e.read().decode(errors='replace')[:2000]}")
    with r:
        return r.read()


def upload(path):
    """Upload a local image to ComfyUI's input folder and return its name there."""
    boundary = uuid.uuid4().hex
    name = f"jenny-{uuid.uuid4().hex[:8]}-{Path(path).name}"
    body = (
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"image\"; filename=\"{name}\"\r\n"
        f"Content-Type: application/octet-stream\r\n\r\n"
    ).encode() + Path(path).read_bytes() + (
        f"\r\n--{boundary}\r\nContent-Disposition: form-data; name=\"overwrite\"\r\n\r\ntrue"
        f"\r\n--{boundary}--\r\n"
    ).encode()
    res = json.loads(_req("/upload/image", body, {"Content-Type": f"multipart/form-data; boundary={boundary}"}))
    return res["name"]


def queue(graph):
    body = json.dumps({"prompt": graph, "client_id": "jenny"}).encode()
    res = json.loads(_req("/prompt", body, {"Content-Type": "application/json"}))
    if res.get("node_errors"):
        sys.exit(f"ComfyUI rejected the graph: {json.dumps(res['node_errors'])}")
    return res["prompt_id"]


def wait(prompt_id, timeout=1800):
    start = time.time()
    while time.time() - start < timeout:
        hist = json.loads(_req(f"/history/{prompt_id}"))
        if prompt_id in hist:
            entry = hist[prompt_id]
            status = entry.get("status", {})
            if status.get("status_str") == "error":
                sys.exit(f"ComfyUI run {prompt_id} failed: {json.dumps(status.get('messages'))[:2000]}")
            for out in entry["outputs"].values():
                for img in out.get("images", []):
                    q = urllib.parse.urlencode(img)
                    return _req(f"/view?{q}")
        time.sleep(2)
    sys.exit(f"timed out waiting for {prompt_id}")


def run_variations(build, n, out_dir, prefix):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    jobs = []
    for i in range(1, n + 1):
        seed = random.randint(1, 2**50)
        jobs.append((i, seed, queue(build(seed, f"jenny-{prefix}"))))
    paths = []
    for i, seed, pid in jobs:
        path = out_dir / f"{prefix}-{i:02d}-seed{seed}.png"
        path.write_bytes(wait(pid))
        paths.append(path)
        print(path, flush=True)
    return paths


def zimage_graph(prompt):
    def build(seed, prefix):
        return {
            "1": {"class_type": "UnetLoaderGGUF", "inputs": {"unet_name": "z-image/z-image-turbo-q4_k_s.gguf"}},
            "2": {"class_type": "ModelSamplingAuraFlow", "inputs": {"model": ["1", 0], "shift": 3, "sampling": "flow"}},
            "3": {"class_type": "CLIPLoaderGGUF", "inputs": {"clip_name": "qwen-4b-zimage-heretic-q8.gguf", "type": "lumina2"}},
            "4": {"class_type": "VAELoader", "inputs": {"vae_name": "ae.safetensors"}},
            "5": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["3", 0], "text": prompt}},
            "6": {"class_type": "ConditioningZeroOut", "inputs": {"conditioning": ["5", 0]}},
            "7": {"class_type": "EmptySD3LatentImage", "inputs": {"width": 1024, "height": 1024, "batch_size": 1}},
            "8": {"class_type": "KSampler", "inputs": {
                "model": ["2", 0], "positive": ["5", 0], "negative": ["6", 0], "latent_image": ["7", 0],
                "seed": seed, "steps": 5, "cfg": 1, "sampler_name": "dpmpp_sde", "scheduler": "beta", "denoise": 1}},
            "9": {"class_type": "VAEDecode", "inputs": {"samples": ["8", 0], "vae": ["4", 0]}},
            "10": {"class_type": "SaveImage", "inputs": {"images": ["9", 0], "filename_prefix": prefix}},
        }
    return build


def klein_base(prompt, model_ref=("1", 0), clip_ref=("2", 0)):
    return {
        "1": {"class_type": "UnetLoaderGGUF", "inputs": {"unet_name": "flux-2-klein-4b-Q4_K_M.gguf"}},
        "2": {"class_type": "CLIPLoaderGGUF", "inputs": {"clip_name": "Qwen3-4B-Q4_K_M.gguf", "type": "flux2"}},
        "3": {"class_type": "VAELoader", "inputs": {"vae_name": "flux2-vae.safetensors"}},
        "4": {"class_type": "CLIPTextEncode", "inputs": {"clip": list(clip_ref), "text": prompt}},
        "5": {"class_type": "ConditioningZeroOut", "inputs": {"conditioning": ["4", 0]}},
        "6": {"class_type": "EmptyFlux2LatentImage", "inputs": {"width": WIDE_W, "height": WIDE_H, "batch_size": 1}},
    }


def klein_sample(g, model_ref, pos_ref, neg_ref, seed, prefix):
    g["90"] = {"class_type": "KSampler", "inputs": {
        "model": list(model_ref), "positive": list(pos_ref), "negative": list(neg_ref), "latent_image": ["6", 0],
        "seed": seed, "steps": 4, "cfg": 1, "sampler_name": "euler", "scheduler": "simple", "denoise": 1}}
    g["91"] = {"class_type": "VAEDecode", "inputs": {"samples": ["90", 0], "vae": ["3", 0]}}
    g["92"] = {"class_type": "SaveImage", "inputs": {"images": ["91", 0], "filename_prefix": prefix}}
    return g


def pad_to_wide(src, dst):
    """Scale the square pick to the target height and centre it on a gray 2:1 canvas."""
    img = Image.open(src).convert("RGB")
    scale = WIDE_H / img.height
    img = img.resize((round(img.width * scale), WIDE_H), Image.LANCZOS)
    canvas = Image.new("RGB", (WIDE_W, WIDE_H), PAD_GRAY)
    x = (WIDE_W - img.width) // 2
    canvas.paste(img, (x, 0))
    canvas.save(dst)
    return img, x


def stitch(generated, original, x, feather=64):
    """Put the pristine original back over the generated centre, fading its side edges."""
    out = Image.open(generated).convert("RGB").resize((WIDE_W, WIDE_H), Image.LANCZOS)
    mask = Image.new("L", original.size, 0)
    ImageDraw.Draw(mask).rectangle([feather, 0, original.width - feather, original.height], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(feather / 2))
    out.paste(original, (x, 0), mask)
    out.save(generated)


def cmd_txt2img(a):
    run_variations(zimage_graph(a.prompt), a.n, a.out, "step1")


def cmd_outpaint(a):
    out_dir = Path(a.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    padded = out_dir / "step2-padded.png"
    original, x = pad_to_wide(a.image, padded)
    ref = upload(padded)

    def build(seed, prefix):
        g = klein_base(OUTPAINT_PROMPT, clip_ref=("7", 1))
        g["7"] = {"class_type": "LoraLoader", "inputs": {
            "model": ["1", 0], "clip": ["2", 0], "lora_name": "klein4b/pixaoutpaint.safetensors",
            "strength_model": 1, "strength_clip": 1}}
        g["10"] = {"class_type": "LoadImage", "inputs": {"image": ref}}
        g["11"] = {"class_type": "VAEEncode", "inputs": {"pixels": ["10", 0], "vae": ["3", 0]}}
        g["12"] = {"class_type": "ReferenceLatent", "inputs": {"conditioning": ["4", 0], "latent": ["11", 0]}}
        g["13"] = {"class_type": "ReferenceLatent", "inputs": {"conditioning": ["5", 0], "latent": ["11", 0]}}
        return klein_sample(g, ("7", 0), ("12", 0), ("13", 0), seed, prefix)

    for path in run_variations(build, a.n, out_dir, "step2"):
        if not a.no_stitch:
            stitch(path, original, x)


def cmd_style(a):
    content, style = upload(a.image), upload(a.style)

    def build(seed, prefix):
        g = klein_base(a.prompt)
        g["10"] = {"class_type": "LoadImage", "inputs": {"image": content}}
        g["11"] = {"class_type": "ImageScaleToTotalPixels", "inputs": {
            "image": ["10", 0], "upscale_method": "nearest-exact", "megapixels": 1, "resolution_steps": 1}}
        g["12"] = {"class_type": "VAEEncode", "inputs": {"pixels": ["11", 0], "vae": ["3", 0]}}
        g["20"] = {"class_type": "LoadImage", "inputs": {"image": style}}
        g["21"] = {"class_type": "ImageScaleToTotalPixels", "inputs": {
            "image": ["20", 0], "upscale_method": "nearest-exact", "megapixels": 1, "resolution_steps": 1}}
        g["22"] = {"class_type": "VAEEncode", "inputs": {"pixels": ["21", 0], "vae": ["3", 0]}}
        # Same chain as the UI workflow: content reference first, then style reference.
        g["30"] = {"class_type": "ReferenceLatent", "inputs": {"conditioning": ["4", 0], "latent": ["12", 0]}}
        g["31"] = {"class_type": "ReferenceLatent", "inputs": {"conditioning": ["30", 0], "latent": ["22", 0]}}
        g["32"] = {"class_type": "ReferenceLatent", "inputs": {"conditioning": ["5", 0], "latent": ["12", 0]}}
        g["33"] = {"class_type": "ReferenceLatent", "inputs": {"conditioning": ["32", 0], "latent": ["22", 0]}}
        return klein_sample(g, ("1", 0), ("31", 0), ("33", 0), seed, prefix)

    run_variations(build, a.n, a.out, "step3")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("txt2img")
    s.add_argument("--prompt", required=True)
    s.add_argument("--n", type=int, default=4)
    s.add_argument("--out", required=True)
    s.set_defaults(func=cmd_txt2img)

    s = sub.add_parser("outpaint")
    s.add_argument("--image", required=True, help="the step 1 pick (square)")
    s.add_argument("--n", type=int, default=3)
    s.add_argument("--out", required=True)
    s.add_argument("--no-stitch", action="store_true", help="keep the model's centre instead of the pristine original")
    s.set_defaults(func=cmd_outpaint)

    s = sub.add_parser("style")
    s.add_argument("--image", required=True, help="the step 2 pick (1440x720)")
    s.add_argument("--style", required=True, help="style reference image")
    s.add_argument("--prompt", required=True, help="short scene + gray style block")
    s.add_argument("--n", type=int, default=4)
    s.add_argument("--out", required=True)
    s.set_defaults(func=cmd_style)

    a = p.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
