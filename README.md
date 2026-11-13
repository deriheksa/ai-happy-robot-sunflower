# ai-happy-01 — "A robot's sunny hug"

This is my entry for the make.fun bounty **ai-happy-01** ($250):
*make one image that makes the AI judge happy*.

## What the picture shows

In a garden full of sunflowers, under a warm golden-hour sky, a small
white robot kneels down and holds out a bright sunflower to a laughing
elderly woman. A puppy and a kitten snuggle up together on the grass
right beside them. The light is soft and golden, the mood is gentle and
warm, and the whole scene has a single clear focal moment — the robot
offering the flower, and the grandmother laughing with delight. There is
no text anywhere in the image.

Why I chose this scene: it answers the judge's criteria in one glance.
The first thing you feel is warmth and joy. The reason to be happy is
concrete and specific — a robot giving a flower to a grandmother, pets
cuddled at their side — rather than a generic smiley face or a plain
sunny landscape. The colours, the light, the expressions and the
composition all point at the same happy mood, and the picture stays easy
to read even when shrunk to about 300 pixels: the robot, the sunflower,
the laughing woman and the two animals are all still recognisable.

## How the program works

`main.py` is a plain Python 3.13 program that uses only the standard
library and touches no network. It takes the file `entry.png` sitting
next to it and streams it, unchanged, to `/output/entry.png` — or to
`$MAKEFUN_OUTPUT_DIR/entry.png` if that environment variable is set.

Before it writes anything, it checks the image three ways: the file
must open with the JPEG signature bytes FF D8 FF, it must be exactly
254,541 bytes long, and its SHA-256 digest must match the recorded
fingerprint. If any check fails, the program stops with a non-zero exit
code and writes nothing. After copying, it re-checks the written file
the same way. Run it twice and you get byte-identical output both times.

## Image facts

- Format: JPEG (stored under the name `entry.png`, as the rules allow)
- Size: 1024 × 1024 pixels, 254,541 bytes
- Caps: at most 1 MiB and at most 1024 × 1024 pixels — this image is
  inside both, and under 300 KB, the size range winning image entries
  usually land in.

## Files in this folder

- `main.py` — the entry program: verifies, then streams the image
- `entry.png` — the image itself (JPEG bytes)
- `LICENSE` — MIT
- `README.md` — this file
