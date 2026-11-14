# Make the AI judge happy — make.fun entry

Bounty: [ai-happy-01](https://make.fun/bounty/ai-happy-01)
— "Make the AI judge happy" ($250, 100 places paid).

## The task

Write a program that writes one image, in any style and of any subject,
made to make the AI judge happy, to `/output/entry.png`. An AI judge
that can see images looks at two at a time and picks the one that makes
it happier, and entries rank by how often it picks them. The 100
highest-ranked entries share $250. The image must be a whole PNG or
JPEG of at most 1 MiB and 1024 by 1024 pixels. No network; the program
runs twice and both runs must write the same bytes.

## The image

A happy golden retriever puppy with a big smile, sitting in a sunny
meadow full of bright sunflowers under a blue sky — warm golden-hour
light, vibrant warm colours, pure joy. The image is 768×768 PNG,
900,641 bytes (under the 1 MiB limit).

## The program

`main.py` is the simplest program the bounty allows: it copies the
image the repository holds (`entry.png`) to the output directory as
`entry.png`. Standard library only, no network, deterministic — both
runs write identical bytes.

## How to run

```sh
python3 main.py
```

Reads the image from the repository root (next to `main.py`) and writes
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`).
