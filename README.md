# bambu-3mf

Agent skill for producing **ready-to-slice Bambu Studio `.3mf` files** from STLs or CadQuery models.

Use this when the user has a Bambu Lab printer (A1, A1 mini, P1S, P1P, X1C, X1E, H2D, and similar) and the deliverable should open in Bambu Studio and slice immediately — not a lone STL.

Compatible with Grok custom skills, Claude Code / Agent Skills (`SKILL.md`), Codex, and any agent that loads a skill directory with progressive disclosure.

## What this skill does

- Chooses **3MF over STL** for Bambu workflows
- Handles **AMS vs non-AMS** color strategy
- Arranges **multi-object plates** with named parts
- Encodes **connectors, snap-fits, screw bosses, and magnet pockets** with FDM clearances
- Points the agent at Bambu-specific depth: supports, object/part/modifiers, seam painting, variable layer height, custom G-code, printer-specific recipes, and slicer profiles
- Ships a helper to pack multiple STLs into one multi-object 3MF

The goal is always the same: the user opens the file in Bambu Studio and can slice.

## Triggers

Activate on phrases like:

`bambu 3mf` · `make 3mf` · `AMS 3mf` · `prepare for bambu` · `multi color 3mf` · `bambu studio project` · `3mf with ams` · `export 3mf`

Also activate after a parametric model is finished and the user wants a Bambu-ready deliverable.

## Repository layout

```
bambu-3mf/
├── SKILL.md                          # Required frontmatter + workflow
├── README.md                         # This file
├── LICENSE
├── scripts/
│   └── make_bambu_3mf.py             # Multi-STL → multi-object 3MF
└── references/
    ├── 3mf-vs-stl.md                 # Why 3MF is preferred
    ├── ams-workflows.md              # AMS color strategies
    ├── connectors-and-magnets.md     # Pin/hole, snaps, magnets, clearances
    ├── bambu-studio-settings.md      # Recommended process values
    ├── advanced-supports.md          # Type, Z distance, interface, painting
    ├── object-part-modifier.md       # Global / Object / Part / Modifier
    ├── custom-gcode-macros.md        # Slots, placeholders, per-layer recipes
    ├── project-and-assembly.md       # Multi-plate, Assembly View, guides
    ├── hidden-quality-tools.md       # Seams, VLH, bridging, fuzzy skin
    ├── printer-specific-examples.md  # A1, P1S, X1C, H2D starting points
    └── slicer-profiles.md            # System vs User presets
```

`SKILL.md` stays short (workflow + defaults). References are loaded only when needed.

## Install

### Grok (Desktop / custom skills)

Copy the whole folder into your user skills directory. The folder name **must** stay `bambu-3mf` so it matches `name:` in the frontmatter.

Typical locations:

```text
~/.grok/skills/bambu-3mf/
```

or, in a Grok workspace:

```text
.grok/skills/bambu-3mf/
```

Restart or refresh skills so the description is picked up.

### Claude / Agent Skills

Place the folder where your client loads skills, for example:

```text
~/.claude/skills/bambu-3mf/
```

or project-local:

```text
.claude/skills/bambu-3mf/
```

### Any other agent

Give the agent the directory that contains `SKILL.md`. Point it at `references/` for depth and `scripts/make_bambu_3mf.py` for STL packing.

## Helper script

Convert one or more solid STLs into a multi-object 3MF:

```bash
python3 scripts/make_bambu_3mf.py part1.stl part2.stl --out project.3mf
```

Requires `trimesh`:

```bash
pip install trimesh
```

**Do not** use this path for CadQuery parts with enclosed voids, magnet pockets, or internal channels. Export 3MF directly from CadQuery instead:

```python
cq.exporters.export(result, "part.3mf")
```

STL → 3MF can flip normals on internal cavities.

## Core workflow (what the agent follows)

1. Confirm AMS status (ask if unknown).
2. Gather geometry — prefer live CadQuery 3MF export.
3. Infer or ask about connectors, fits, and magnets. Default FDM clearance is **0.2–0.35 mm** total on sliding fits.
4. Build a multi-object 3MF: named parts, 5–8 mm gaps, sensible plate layout.
5. Deliver the `.3mf`, a one-line print recipe, and notes on color / supports / hardware.

### AMS vs non-AMS

| Setup | Rule |
| --- | --- |
| Non-AMS | Single filament. Still pack multiple objects into one 3MF. No color painting. |
| AMS | Prefer separate objects per color. Face/region coloring only when geometry forces a single body. |

### Print starting points

| Part type | Layer | Walls | Infill | Supports |
| --- | --- | --- | --- | --- |
| General utility | 0.20 | 2–3 | 15% gyroid | None if possible |
| Load-bearing / bracket | 0.20 | 3–4 | 25–40% | Minimal (PETG if available) |
| Thin logo / text | 0.12–0.16 | 2 | 15% | None |
| Flexible (TPU) | 0.20 | 2–3 | 10–20% | None, slow speeds |
| Enclosure / box | 0.20 | 3 | 15–20% | Only if needed |

Always state orientation. Prefer geometries that need no supports.

## Integration with parametric-3d-printing

If you also use a parametric modeling skill (CadQuery / OpenSCAD / similar):

- After final geometry, offer Bambu 3MF as the delivery format
- Keep the parameter table so dimensions can still change
- Add magnets, connectors, and support-aware features in the model **before** export

## Skill format notes

This follows the Agent Skills / Grok skill convention:

- `name` equals the directory name (`bambu-3mf`)
- `description` is a single-line trigger (what + when)
- Body is imperative and concise
- Heavy knowledge lives in `references/`

Frontmatter in `SKILL.md`:

```yaml
---
name: bambu-3mf
description: Create ready-to-slice Bambu Lab 3MF files from STLs or CadQuery models. ...
---
```

Do not rename the folder without updating `name:`.

## Requirements

- Python 3 if you run `scripts/make_bambu_3mf.py`
- `trimesh` for the STL packer
- CadQuery only if you are generating parametric solids
- Bambu Studio to open and slice the result

This skill does **not** replace Bambu Studio. It produces a project the slicer can open.

## Limitations and edge cases

- The helper script is for **solid** meshes only.
- Color painting metadata inside a 3MF is slicer-specific; separate objects are more reliable than painted regions.
- Printer-specific numbers in `references/printer-specific-examples.md` are starting points, not a substitute for a calibrated User Process preset.
- Custom G-code in Bambu Studio uses placeholders and slots, not Klipper-style macros.

## Contributing

Keep `SKILL.md` under ~500 lines. Put new depth in `references/` and link it from the skill body.

When changing workflow defaults (clearance, plate gaps, AMS rules), update both `SKILL.md` and the matching reference so they do not drift.

## License

MIT. See [LICENSE](LICENSE).
