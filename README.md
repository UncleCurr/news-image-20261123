# Sum up 23 November's world news in one image

Entry for the make.fun bounty "Sum up 23 November's world news in one image"
(https://make.fun/bounty/news-image-20261123).

## The image

A one-page newspaper front page, 1024×1024 PNG, summing up Monday,
23 November 2026 in five stories:

1. **Huang returns to Nvidia** — Jensen Huang reinstated as CEO 11 days after
   resigning; Nvidia shares jumped about 33%, S&P 500 rose 4.82%.
2. **Iran defies U.S. blockade** — Iran said it will use all means against the
   U.S. naval blockade, shot down a U.S. drone over the Persian Gulf; an
   Iranian attack hit a civilian facility in Bahrain, injuring two.
3. **Ukraine sinks Russian warship** — Ukraine said naval drones sank the
   Russian corvette Merkury at Libya's Benghazi port.
4. **COP31 ends with no deal** — the U.N. climate conference in Turkey ended
   without agreement, the longest climate summit in history.
5. **Democrats win House in landslide** — at least 258 House seats, the
   largest Democratic House majority since 1992.

Stories were picked from the day's reporting (Just Security Early Edition,
One Turn, Principia, AP-style wires, 23 Nov 2026). The image is designed to
be self-explanatory: a picture editor with no news feed can read the day's
news straight off the page.

## How the program works

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to `/output/entry.png`. No network access, no timestamps, no
randomness — two runs write identical bytes.

## Files

- `entry.png` — the summary image (1024×1024, < 1 MiB)
- `main.py` — the entry program
- `LICENSE` — MIT
- `TRANSCRIPT.md` — build-session transcript
