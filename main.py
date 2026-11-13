"""ai-happy-01 entry: "A robot's sunny hug".

Writes one image made to make the AI judge happy to /output/entry.png.
The image is the file entry.png next to this program (a JPEG, kept under
the competition's 1 MiB / 1024x1024 caps, 1024x1024); this program verifies
its SHA-256, size and JPEG magic bytes, then streams it unchanged to the
output, so both runs write byte-identical output.
Python 3.13, standard library only, no network, no randomness, no timestamps.
"""

import hashlib
import os
import sys

EXPECTED_SHA256 = "5a8e724d9bb34ead38b16e1df2f808f68cd6a24b7a7405fdb9d36cdb5864f287"
EXPECTED_SIZE = 254541  # bytes; kit cap is 1048576, image is 1024x1024
CHUNK = 65536


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)

    digest = hashlib.sha256()
    size = 0
    with open(src, "rb") as f:
        magic = f.read(3)
        if magic != b"\xff\xd8\xff":
            sys.exit("entry.png is not a JPEG (bad magic bytes)")
        digest.update(magic)
        size += 3
        while True:
            chunk = f.read(CHUNK)
            if not chunk:
                break
            digest.update(chunk)
            size += len(chunk)

    if size != EXPECTED_SIZE:
        sys.exit("size mismatch: got %d, expected %d" % (size, EXPECTED_SIZE))
    if digest.hexdigest() != EXPECTED_SHA256:
        sys.exit("sha256 mismatch: image bytes failed integrity check")

    written = 0
    with open(src, "rb") as f, open(out_path, "wb") as out:
        while True:
            chunk = f.read(CHUNK)
            if not chunk:
                break
            out.write(chunk)
            written += len(chunk)

    print("wrote %s (%d bytes, sha256 %s)" % (out_path, written, EXPECTED_SHA256[:16]))


if __name__ == "__main__":
    main()
