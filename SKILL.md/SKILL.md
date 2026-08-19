---
name: bambu-3mf
description: Create ready-to-slice Bambu Lab 3MF files from STLs or CadQuery models. Handles AMS vs non-AMS, multi-object plate arrangement, project/assembly workflows, connectors, magnets, advanced supports, object/part/modifier settings, seam painting, variable layer height, custom G-code, printer-specific recommendations, slicer profiles, quality and strength. Triggers on bambu 3mf, make 3mf, AMS 3mf, prepare for bambu, multi color 3mf, bambu studio project, 3mf with ams, export 3mf.
---

# Bambu 3MF

Produce Bambu Studio `.3mf` files that open ready to slice. Prefer 3MF over STL whenever the user has a Bambu Lab printer (A1, A1 mini, P1S, X1C, etc.).

## When to use this skill

Activate on any request for Bambu-ready files, AMS multi-color preparation, plate arrangement, or print-ready projects. Also activate when the user finishes a parametric model and wants the final deliverable for their Bambu printer.

## Core Workflow

1. **Confirm AMS status** (ask if unknown)
   - Non-AMS → single filament, multi-object 3MF still preferred
   - AMS → separate objects for different colors (best reliability). Simple face/region separation is acceptable when a single body needs multiple colors.

2. **Gather geometry**
   - Prefer live CadQuery solids from `parametric-3d-printing`. Export 3MF directly:
     ```python
     cq.exporters.export(result, "part.3mf")
     ```
     This preserves internal cavities correctly.
   - Fallback only for simple solid STLs (no enclosed voids). Use the helper script with caution.

3. **Connectors, fits & magnets**
   - Infer or ask whether parts need to join.
   - Default patterns (see `references/connectors-and-magnets.md`):
     - Pin + hole (most common, reliable)
     - Snap-fit / cantilever
     - Screw bosses (prefer heat-set inserts)
     - Magnet pockets (6×2 mm or 6×3 mm standard)
   - Always apply FDM clearance (0.2–0.35 mm total on sliding fits).
   - For “easy fitting” requests, use the classic hole-on-one-part + extruded-pin-on-the-other pattern with a small lead-in chamfer.

4. **Build the 3MF**
   - Multi-object when multiple parts exist.
   - Arrange parts on the build plate with sensible spacing (5–8 mm gaps).
   - Name objects clearly (`tray`, `logo_plaque`, `drain_plug`, etc.).
   - Goal: user opens the file in Bambu Studio and can slice immediately.

5. **Deliver**
   - The `.3mf` file(s)
   - One-line print recipe (material, layer height, walls, infill, supports, orientation)
   - Short notes on connectors, magnets, AMS colors, or support strategy if relevant

## AMS vs Non-AMS Rules

**Non-AMS**
- Single filament.
- Still pack multiple objects into one 3MF so they print together.
- No color painting.

**AMS**
- Prefer separate objects for different colors.
- Only use simple face/region coloring when geometry forces a single body.
- Tell the user which object should receive which color when you have a clear recommendation.

## Advanced Control

### Project & Assembly
Bambu Studio’s project system (multi-plate, Assembly View, Assembly Guides) is a major unique strength.
See `references/project-and-assembly.md`. Prefer clear object names and logical plate separation.

### Supports
Prefer geometries that need no supports. When supports are required, follow the decision tree and recommended profiles in `references/advanced-supports.md`.

Key priorities:
- Choose Tree (Organic) or Hybrid for most parts
- Tune Top Z Distance and Interface Layers for clean removal vs surface quality
- Use Support Painting when auto generation is imperfect

### Object / Part / Modifier
Use the lowest level that achieves the goal (see `references/object-part-modifier.md`):
- Global → defaults
- Object → different settings per model
- Part → different settings inside a multi-body object
- Modifier → local region changes (higher infill in stress zones, etc.)

When exporting 3MFs, keep clear object names so the user can easily apply Object-level overrides later.

### Hidden Quality Tools
Seam Painting, Variable Layer Height, Counterbore Hole Bridging, and Fuzzy Skin Painting dramatically improve results when used correctly.
See `references/hidden-quality-tools.md`.

### Custom G-code / Macros
Bambu Studio uses custom G-code slots + placeholders rather than Klipper-style macros.
See `references/custom-gcode-macros.md` for:
- All available G-code slots
- Useful placeholders and conditionals
- Per-layer custom G-code (easiest method)
- Practical recipes (magnet pauses, temperature towers, speed changes, no-unload end gcode)

### Printer-Specific Guidance
Different Bambu printers have different strengths. See `references/printer-specific-examples.md` for tailored starting points (A1, P1S, X1C, H2D, etc.).
When the user’s printer is known, prefer those recommendations.

### Slicer Profiles
Understand System vs User presets and inheritance. See `references/slicer-profiles.md`.
Prefer cloning system profiles rather than editing them. Suggest creating User Process presets when recommendations deviate meaningfully from stock.

## CadQuery Export Preference

Always prefer native CadQuery 3MF export over STL conversion when the model was built in CadQuery. The STL→3MF path can flip normals on internal cavities.

## Print Defaults (starting points)

| Part type              | Layer     | Walls | Infill      | Supports         | Notes                     |
|------------------------|-----------|-------|-------------|------------------|---------------------------|
| General utility        | 0.20      | 2–3   | 15% gyroid  | None if possible |                           |
| Load-bearing / bracket | 0.20      | 3–4   | 25–40%      | Minimal          | Prefer PETG if available  |
| Thin logo / text       | 0.12–0.16 | 2     | 15%         | None             |                           |
| Flexible (TPU)         | 0.20      | 2–3   | 10–20%      | None             | Slow speeds               |
| Enclosure / box        | 0.20      | 3     | 15–20%      | Only if needed   |                           |

Always state orientation. Prefer geometries that need no supports.

## Integration with parametric-3d-printing

- After Phase 3 (final geometry) of any parametric model, offer the Bambu 3MF as the delivery format.
- Keep the parameter table so the user can still request dimensional tweaks.
- When magnets, connectors, or special support needs are requested, add them in the CadQuery script before exporting 3MF.

## Helper Scripts

- `scripts/make_bambu_3mf.py` — multi-STL → multi-object 3MF
- `parametric-3d-printing/stl_to_3mf.py` — only for simple solid meshes (no cavities)

## References

- `references/3mf-vs-stl.md` — why 3MF is preferred
- `references/ams-workflows.md` — AMS color strategies
- `references/connectors-and-magnets.md` — pin/hole, snaps, magnet pockets, clearances
- `references/bambu-studio-settings.md` — recommended process values
- `references/advanced-supports.md` — support type, Z distance, interface, painting
- `references/object-part-modifier.md` — Global / Object / Part / Modifier control
- `references/custom-gcode-macros.md` — custom G-code slots, placeholders, per-layer macros
- `references/project-and-assembly.md` — multi-plate projects, Assembly View, Assembly Guides
- `references/hidden-quality-tools.md` — Seam Painting, Variable Layer Height, Counterbore Bridging, Fuzzy Skin
- `references/printer-specific-examples.md` — A1, P1S, X1C, H2D tailored recommendations
- `references/slicer-profiles.md` — System vs User presets, inheritance, creating custom profiles
