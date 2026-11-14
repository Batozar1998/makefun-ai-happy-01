#!/usr/bin/env python3
"""make.fun entry: ai-happy-01 — Make the AI judge happy.

The entry is a program that writes one image to /output/entry.png.
The image is a happy golden retriever puppy smiling in a sunny
sunflower meadow — bright, warm, and joyful. The program simply copies
the image the repository holds (entry.png) to the output directory, so
both runs write identical bytes.

Standard library only, no network, deterministic.
Reads the image from the repository root (next to this file) and writes
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
"""

import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT_IMAGE = os.path.join(HERE, "entry.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
MAX_BYTES = 1024 * 1024
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def png_size(path):
    """Return (width, height) of a PNG by reading its IHDR chunk."""
    with open(path, "rb") as f:
        header = f.read(33)
    if header[:8] != PNG_MAGIC or header[12:16] != b"IHDR":
        raise ValueError("not a PNG file")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main():
    if not os.path.isfile(INPUT_IMAGE):
        print("missing input image: %s" % INPUT_IMAGE, file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out = os.path.join(OUTPUT_DIR, "entry.png")
    shutil.copyfile(INPUT_IMAGE, out)
    # Self-check the output the judge will see: a whole PNG, within
    # the 1 MiB and 1024x1024 limits, identical to the input.
    size = os.path.getsize(out)
    if size > MAX_BYTES:
        print("output too large: %d bytes" % size, file=sys.stderr)
        return 1
    width, height = png_size(out)
    if width > MAX_SIDE or height > MAX_SIDE:
        print("output too large: %dx%d" % (width, height), file=sys.stderr)
        return 1
    if open(out, "rb").read() != open(INPUT_IMAGE, "rb").read():
        print("output differs from input", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
