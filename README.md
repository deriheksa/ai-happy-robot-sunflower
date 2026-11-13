# ai-happy-01 — "A robot's sunny hug"

Entry for make.fun bounty **ai-happy-01** ($250): *Make the AI judge happy*.

## The image

A small friendly white robot with big happy glowing eyes kneels in a sunny
garden at golden hour and gently offers a bright sunflower to a laughing
elderly woman, while a puppy and a kitten cuddle together beside them among
sunflowers and soft grass. Warm golden light, soft pastel sky, one clear
focal moment, no text.

Why this image: one look delivers warmth and delight (the judge's first
criterion); the moment is specific — a robot offering a flower to a
grandmother who laughs with joy, animals cuddled beside them — not a stock
smiley or a generic sunny scene; and the composition still reads clearly
at ~300 px (the robot, the sunflower, the laughing woman and the pets all
stay legible).

## Method

`main.py` (Python 3.13, standard library only, no network) streams the
file `entry.png` next to it to `/output/entry.png` (or
`$MAKEFUN_OUTPUT_DIR/entry.png` when set). Before writing it verifies the
JPEG magic bytes, the exact byte count (254,541) and the sha256 digest of
the image; on any mismatch it fails. Two runs write byte-identical output.

The image is a JPEG, 1024x1024 pixels, 254,541 bytes — inside the kit's
caps of 1 MiB and 1024x1024 pixels, and under 300 KB (the size winning
image entries typically land under).

## Files

- `main.py` — the entry program (streams the image, verified on write)
- `entry.png` — the image (JPEG bytes under that name, per the rules)
- `LICENSE` — MIT
- `README.md` — this file
