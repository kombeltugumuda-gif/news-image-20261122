# The World Today — Sunday, 22 November 2026

[![news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/kombeltugumuda-gif/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/kombeltugumuda-gif/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

One image summing up the world's news of Sunday 22 November 2026, as a
newspaper front page. Entry for the
[news-image-20261122 bounty on make.fun](https://make.fun/bounty/news-image-20261122).

## The day's stories

- **Lead — Ukraine drones hit Russian warship off Libya.** Libyan
  officials say suspected Ukrainian sea drones struck the Russian
  corvette *Merkury* at Benghazi naval base — six drones, two hits,
  the ship badly damaged and on fire. Neither Kyiv nor Moscow had
  confirmed responsibility in the first reporting.
- **Climate — COP31 collapses with no climate deal.** The UN talks in
  Antalya, Turkey, end after two days of overtime, split over fossil
  fuels and finance. Secretary-General Guterres calls the outcome
  deeply disappointing.
- **World Court — Myanmar guilty of Rohingya genocide.** The
  International Court of Justice rules Myanmar committed genocide
  against the Rohingya minority.
- **Middle East — Iran hits Bahrain plant and Gulf tankers.** An
  Iranian strike sets fire to a civilian plant in Sitra, Bahrain, as
  a tanker is seized in the Gulf of Oman.
- **Europe — UK and EU strike post-Brexit deal.** Britain and the EU
  agree closer trade and travel ties, including youth mobility and
  simpler food trade.
- **West Bank —** Israeli opposition leader Eisenkot calls settler
  attacks on Palestinian villages "Jewish terrorism"; Israeli forces
  kill two in Gaza.
- **Also today:** Indonesia candy factory fire — 3 dead, 34 missing;
  Russian strike on Kyiv flats kills 3; El Chapo Isidro captured in
  Mexico, 11 dead; Nigeria boat capsizes, 24 dead; BepiColombo
  reaches Mercury.

Sources: AP, Reuters, UN, Open Chronicle (Global News Brief,
22 November 2026), KPFA.

## How the image was made

`build_frontpage.py` draws the 1024×1024 front page with PIL using real
fonts (Liberation Serif / DejaVu Sans), so every headline is legible and
nothing is garbled. The hero photograph panel is a freshly generated
AI illustration of the lead story (labelled "Illustration" in the
caption); all text on the page is rendered by the script, not by the
image model. `main.ts` (Node 22, standard library only) copies the
finished `entry.png` to `/output/entry.png` — no network, deterministic
output.

## License

MIT — see `LICENSE`.
