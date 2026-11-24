#!/usr/bin/env python3
"""Entry for make.fun bounty "Sum up 23 November's world news in one image".

Writes the pre-built news-summary image to /output/entry.png, then
verifies the output is a valid PNG of 1024x1024 pixels and under 1 MiB,
as the bounty requires.

Deterministic: the same input bytes are copied on every run. No network
access, no timestamps, no randomness. Only the Python standard library.
"""

import os
import shutil
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path("/output/entry.png")
MAX_BYTES = 1024 * 1024
WIDTH = 1024
HEIGHT = 1024


def png_size(path):
    """Return (width, height) of a PNG file, or None if it is not a PNG."""
    with open(path, "rb") as f:
        header = f.read(33)
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    if header[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main() -> int:
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)
    size = os.path.getsize(DST)
    if size > MAX_BYTES:
        print(f"entry.png is {size} bytes, over the 1 MiB limit", file=sys.stderr)
        return 1
    dims = png_size(DST)
    if dims != (WIDTH, HEIGHT):
        print(f"entry.png is {dims}, expected (1024, 1024)", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
