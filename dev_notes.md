# dev_notes.md

## 🧭 Project Direction

**Melee Move Matrix** aims to create a data-driven taxonomy of move types in Super Smash Bros. Melee, grounded in frame data, movement interactions, and competitive function.

This file tracks project decisions, technical notes, ideas, and long-term goals.

---

## ✅ Completed Milestones

- Setup virtual environment with reproducible dependencies
- Parsed raw JSON frame data from all characters
- Output clean `move_summary.csv` as base dataset
- Added `.gitignore`, `requirements.txt`, and structured repo

---

## 🔨 In Progress

- EDA Notebook: explore startup, active frames, IASA, damage
- Classify edge cases: multi-hit, drill-type vs stomp-type, rekka/jab variants
- Document challenges in move encoding (e.g. autocancel, landing lag, reusability)

---

## 🧠 Feature Ideas & Directions

### Functional Tags
- [ ] Add `is_aerial`, `is_grab`, `has_landing_lag`, etc.
- [ ] Estimate `true_endlag` from `total` and `IASA`
- [ ] Tag by hitbox angle and type (anti-air, poke, wall)

### Clustering & Visualization
- [ ] PCA / t-SNE on normalized feature vectors
- [ ] Group moves by startup/damage ratio
- [ ] Cluster move archetypes (e.g. pokes, burst options)

### Utility / Taxonomy
- [ ] Define tactical utility tags (poke, anti-air, bait)
- [ ] Create player-oriented labels: “early burst”, “safe ender”, etc.
- [ ] Cross-character comparisons (e.g. Falcon bair vs Sheik fair)

### Technical Enhancements
- [ ] Extend parser to extract autocancel/landing lag
- [ ] Support parsing hitbox placement (if data exists)
- [ ] Split out move categories into separate CSVs or JSONs

---

## ⚠️ Known Challenges & Caveats

- Multi-hit moves span irregular windows — must encode cleanly
- Some moves have branching logic (e.g. jab1 → jab2, gentleman)
- L-cancel, autocancel, and IASA are overlapping mechanics
- Game & Watch aerials lack L-cancel
