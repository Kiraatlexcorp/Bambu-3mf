# Project-Based Workflow & Assembly

Bambu Studio’s biggest unique advantage is its **project-based 3MF** system. A single 3MF can contain multiple plates, object relationships, colors, modifiers, and even assembly documentation.

## When to use multi-plate projects

- Parts that need different process settings (e.g. logo at 0.12 mm + tray at 0.20 mm)
- Parts that must be printed in different orientations
- Very large assemblies that exceed one plate
- Color separation that benefits from dedicated plates

Keep related parts on the same plate when possible so the user can print them together.

## Assembly View

Available when the original model was imported as a multi-body STEP/STP (or properly structured 3MF).

Use Assembly View when:
- The user will physically assemble the printed parts
- You want to color different logical parts while seeing the final assembled form
- You need to generate an Assembly Guide

Switch freely between **Objects** (print-oriented) and **Assembly** (design-oriented) views.

## Assembly Guide (newer feature)

Bambu Studio can generate step-by-step assembly instructions from a STEP file:
- Automatic step detection
- Camera views and labels
- Export to PDF / Markdown / MP4

Recommend this when delivering complex multi-part functional designs (enclosures, mechanisms, multi-body trays, etc.).

## Best practices for 3MF export from this skill

- Keep clear, logical object names (`tray`, `logo_plaque`, `drain_plug_01`…)
- Prefer multi-object over single fused body when parts are meant to be separate
- Use separate plates only when there is a clear benefit
- If the source was a STEP assembly, preserve the ability to use Assembly View
- Add a short note in the delivery about recommended plate strategy and whether an Assembly Guide would be useful
