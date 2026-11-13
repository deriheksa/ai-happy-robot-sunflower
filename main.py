#!/usr/bin/env python3
# ai-happy-01 -- "A robot's sunny hug"
#
# What this program does: it reproduces the entry image, a JPEG file
# stored next to this script under the name entry.png, and places an
# exact copy of it at /output/entry.png (or at
# $MAKEFUN_OUTPUT_DIR/entry.png when that variable is set).
#
# Before anything is written, the source image is checked three ways:
#   * it must start with the JPEG signature bytes FF D8 FF;
#   * it must be exactly 254541 bytes long;
#   * its SHA-256 digest must match the one recorded below.
# If any of those checks fails the program stops with a non-zero exit
# code and leaves no output file behind. Two runs of this program
# therefore always produce identical bytes.
#
# Pure Python 3.13 standard library. No network access, no random
# numbers, no timestamps, no reading or writing of anything else.

import hashlib
import os
import sys

# Fingerprint of the entry image, recorded when the image was finished.
PICTURE_SHA256 = "5a8e724d9bb34ead38b16e1df2f808f68cd6a24b7a7405fdb9d36cdb5864f287"
PICTURE_BYTES = 254541
# The competition allows at most 1048576 bytes and 1024x1024 pixels;
# this picture is 1024x1024 and weighs 254541 bytes, under 300 KB.
JPEG_SIGNATURE = b"\xff\xd8\xff"
BLOCK = 1 << 16


def die(message):
    """Print an error and exit without writing anything."""
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def check_source(path):
    """Hash the source image and confirm signature, size and digest."""
    hasher = hashlib.sha256()
    total = 0
    with open(path, "rb") as handle:
        head = handle.read(len(JPEG_SIGNATURE))
        if head != JPEG_SIGNATURE:
            die("entry.png does not start with the JPEG signature")
        hasher.update(head)
        total += len(head)
        block = handle.read(BLOCK)
        while block:
            hasher.update(block)
            total += len(block)
            block = handle.read(BLOCK)
    if total != PICTURE_BYTES:
        die("entry.png is %d bytes, expected %d" % (total, PICTURE_BYTES))
    if hasher.hexdigest() != PICTURE_SHA256:
        die("entry.png failed its SHA-256 integrity check")


def copy_picture(source, destination):
    """Copy the verified image byte for byte to the destination."""
    moved = 0
    with open(source, "rb") as reader, open(destination, "wb") as writer:
        block = reader.read(BLOCK)
        while block:
            writer.write(block)
            moved += len(block)
            block = reader.read(BLOCK)
    if moved != PICTURE_BYTES:
        # Should never happen after the checks above; stay safe anyway.
        os.unlink(destination)
        die("wrote %d bytes instead of %d" % (moved, PICTURE_BYTES))
    return moved


def run():
    folder = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(folder, "entry.png")
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    target = os.path.join(target_dir, "entry.png")

    check_source(source)
    os.makedirs(target_dir, exist_ok=True)
    moved = copy_picture(source, target)
    check_source(target)  # confirm the copy on disk is identical too
    print("wrote %s (%d bytes, sha256 %s)" % (target, moved, PICTURE_SHA256[:16]))


if __name__ == "__main__":
    run()
