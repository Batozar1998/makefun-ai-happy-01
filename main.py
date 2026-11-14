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

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT_IMAGE = os.path.join(HERE, "entry.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out = os.path.join(OUTPUT_DIR, "entry.png")
    shutil.copyfile(INPUT_IMAGE, out)


if __name__ == "__main__":
    main()
