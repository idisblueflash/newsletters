#!/usr/bin/env python3
"""Crop a screenshot into a 3:4 小红书 cover (1080x1440) without losing content.

Three modes:
  page    crop to the paper/page area, pad with the page's own background colour
  window  keep the app window (title bar included), pad with the backdrop colour
  full    keep everything, centre-pad to 3:4

Nothing is cropped away in `page` and `window` modes — they pad instead.
`--pad N` adds N source pixels of breathing room around the detected region.

    python3 crop_cover.py in.png out.jpg --mode page
"""
import argparse
from collections import Counter

from PIL import Image

TARGET_W, TARGET_H = 1080, 1440
TARGET_RATIO = TARGET_W / TARGET_H


def luminance(c):
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def bbox_of(im, predicate, scale=4):
    """Bounding box (in source pixels) of every pixel satisfying predicate."""
    small = im.resize((im.width // scale, im.height // scale), Image.NEAREST)
    px = small.load()
    xs, ys = [], []
    for y in range(small.height):
        for x in range(small.width):
            if predicate(px[x, y]):
                xs.append(x)
                ys.append(y)
    if not xs:
        raise SystemExit("nothing matched — try another mode or raise the threshold")
    return (min(xs) * scale, min(ys) * scale,
            (max(xs) + 1) * scale, (max(ys) + 1) * scale)


def dominant_colour(im, box):
    crop = im.crop(box)
    crop.thumbnail((200, 200))
    counts = Counter(crop.getdata())
    return counts.most_common(1)[0][0]


def pad_to_ratio(im, box, pad, colour):
    """Expand box to 3:4 with `colour` only, then resize to the target size.

    `box` is the whole content; everything added beyond it is flat colour, so
    nothing from outside the detected region leaks into the frame.
    """
    x0, y0, x1, y1 = box
    x0, y0, x1, y1 = x0 - pad, y0 - pad, x1 + pad, y1 + pad
    w, h = x1 - x0, y1 - y0

    if w / h < TARGET_RATIO:          # too tall: widen
        want = int(round(h * TARGET_RATIO))
        extra = want - w
        x0, x1 = x0 - extra // 2, x1 + extra - extra // 2
    else:                             # too wide: heighten
        want = int(round(w / TARGET_RATIO))
        extra = want - h
        y0, y1 = y0 - extra // 2, y1 + extra - extra // 2
    w, h = x1 - x0, y1 - y0

    canvas = Image.new("RGB", (w, h), colour)
    sx0, sy0 = max(0, x0), max(0, y0)
    sx1, sy1 = min(im.width, x1), min(im.height, y1)
    if sx1 > sx0 and sy1 > sy0:
        canvas.paste(im.crop((sx0, sy0, sx1, sy1)), (sx0 - x0, sy0 - y0))
    return canvas.resize((TARGET_W, TARGET_H), Image.LANCZOS)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("out")
    ap.add_argument("--mode", choices=["page", "window", "full"], default="page")
    ap.add_argument("--pad", type=int, default=40)
    ap.add_argument("--quality", type=int, default=92)
    args = ap.parse_args()

    im = Image.open(args.src).convert("RGB")

    if args.mode == "full":
        colour = dominant_colour(im, (0, 0, 40, 40))
        box = (0, 0, im.width, im.height)
    elif args.mode == "window":
        colour = dominant_colour(im, (0, 0, 40, 40))
        box = bbox_of(im, lambda c: luminance(c) > 150)
    else:  # page
        # the colour at the centre is the paper on a reading app; keep every
        # pixel within a small distance of it
        colour = im.getpixel((im.width // 2, im.height // 2))
        box = bbox_of(im, lambda c: max(abs(c[i] - colour[i]) for i in range(3)) <= 6)

    if args.mode == "page":
        # trim to the page so the margin is paper, not the app background
        im = im.crop(box)
        box = (0, 0, im.width, im.height)

    canvas = pad_to_ratio(im, box, args.pad, colour)
    canvas.save(args.out, "JPEG", quality=args.quality, optimize=True)
    print(f"{args.mode}: region={box} pad_colour={colour} -> {args.out} "
          f"{canvas.width}x{canvas.height}")


if __name__ == "__main__":
    main()
