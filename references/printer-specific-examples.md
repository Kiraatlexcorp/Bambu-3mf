# Printer-Specific Examples

Practical starting points for the most common Bambu Lab printers. Always confirm the exact nozzle size the user has installed.

## Bambu Lab A1 / A1 mini

**Strengths:** Excellent for single-color and simple multi-color, quiet, great first-layer, easy maintenance.  
**Limits:** Open frame (drafts affect ABS/ASA), smaller build volume on mini.

**Recommended defaults**
- Process: 0.20 mm Standard or 0.16 mm High Quality
- Supports: Tree (Organic), Top Z 0.22–0.25 mm
- Plate: Textured PEI or Cool Plate for PLA
- Best for: Everyday functional parts, logos, trays, organizers

**Special notes**
- A1 mini → keep models under ~180 mm in X/Y when possible
- Very good with matte PLA and basic multi-color (AMS lite)

## Bambu Lab P1S / P1P

**Strengths:** Enclosed, fast, excellent price/performance, good for PETG and mild ABS.  
**Limits:** No lidar (manual flow calibration more important).

**Recommended defaults**
- Process: 0.20 mm Standard / Strength
- Supports: Tree or Hybrid
- For PETG: raise Top Z Distance slightly (0.25–0.28 mm)
- Best for: Functional mechanical parts, enclosures, multi-part projects

**Special notes**
- P1S benefits from the enclosure — prefer PETG or ABS when strength matters
- Good candidate for multi-plate projects

## Bambu Lab X1C / X1E

**Strengths:** Lidar + AI, best automatic calibration, full AMS support, excellent for engineering filaments.  
**Limits:** Higher cost.

**Recommended defaults**
- Process: 0.20 mm Standard or 0.16 mm High Quality
- Let the printer run Flow Dynamics Calibration when possible
- Supports: Tree (Organic) + Support Painting for critical surfaces
- Best for: High-detail logos, engineering parts, complex multi-color

**Special notes**
- Take advantage of lidar for first-layer and flow
- Ideal for projects that use Seam Painting + Variable Layer Height
- Strong candidate for Assembly View + Assembly Guides

## Bambu Lab H2D / dual-nozzle machines

**Strengths:** True dual-nozzle (or toolchanger-style), much lower flush waste, independent parameters per nozzle.  
**Limits:** More complex filament mapping.

**Recommended defaults**
- Use Filament Grouping (Filament-Saving mode when possible)
- Assign high-flush or support material to the secondary nozzle when useful
- Independent process settings per nozzle are available — use them
- Best for: Multi-material, support interface + model material, complex color work

**Special notes**
- Always think in terms of nozzle assignment, not just AMS slots
- Counterbore bridging and interface ironing are especially useful here

## Quick Decision Table

| Printer       | Best for                        | Default Process          | Notes                          |
|---------------|---------------------------------|--------------------------|--------------------------------|
| A1 / A1 mini  | Everyday + simple multi-color   | 0.20 Standard            | Keep it simple                 |
| P1S           | Functional + PETG               | 0.20 Strength            | Use the enclosure              |
| X1C / X1E     | Detail + engineering + complex  | 0.16–0.20 High Quality   | Leverage lidar + painting tools|
| H2D           | Multi-material / low waste      | Per-nozzle settings      | Filament Grouping is key       |

When generating a 3MF, briefly note which printer family the recommendations assume, or ask the user if unknown.
