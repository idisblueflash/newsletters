#!/usr/bin/env python3
"""
Convert PNG (or other raster) images to web-friendly JPEG.

Keeps pixel dimensions unchanged by default — only re-encodes to JPEG with
a quality setting, which is usually where most of the file-size savings
come from for cover-art style images. Pass --max-width to also downscale.

Usage:
    scripts/optimize.py IMAGE [IMAGE ...] [--quality 85] [--max-width N] [--suffix -web] [--out DIR]

Examples:
    scripts/optimize.py cover/cover.png
    scripts/optimize.py cover/cover.png cover/cover-color.png --quality 80
    scripts/optimize.py cover/cover.png --max-width 1200 --suffix -thumb
"""

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow not installed. Run: pip install Pillow", file=sys.stderr)
    sys.exit(1)


def optimize(src: Path, quality: int, max_width: int | None, suffix: str, out_dir: Path | None) -> Path:
    im = Image.open(src)
    if im.mode in ("RGBA", "P", "LA"):
        im = im.convert("RGB")

    if max_width and im.width > max_width:
        new_height = round(im.height * max_width / im.width)
        im = im.resize((max_width, new_height), Image.LANCZOS)

    target_dir = out_dir if out_dir else src.parent
    dst = target_dir / f"{src.stem}{suffix}.jpg"
    im.save(dst, "JPEG", quality=quality, optimize=True)
    return dst


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("images", nargs="+", type=Path, help="Source image path(s)")
    parser.add_argument("--quality", type=int, default=85, help="JPEG quality 1-95 (default 85)")
    parser.add_argument("--max-width", type=int, default=None, help="Downscale if wider than this (default: keep original size)")
    parser.add_argument("--suffix", default="-web", help="Filename suffix before .jpg (default: -web)")
    parser.add_argument("--out", type=Path, default=None, help="Output directory (default: same as source)")
    args = parser.parse_args()

    for src in args.images:
        if not src.exists():
            print(f"Error: file not found: {src}", file=sys.stderr)
            sys.exit(1)

    if args.out:
        args.out.mkdir(parents=True, exist_ok=True)

    for src in args.images:
        before = src.stat().st_size
        dst = optimize(src, args.quality, args.max_width, args.suffix, args.out)
        after = dst.stat().st_size
        pct = 100 * (1 - after / before)
        print(f"{src} ({before // 1024} KB) -> {dst} ({after // 1024} KB, -{pct:.0f}%)")


if __name__ == "__main__":
    main()
