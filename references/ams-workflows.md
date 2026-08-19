# AMS Workflows

## Recommended approach

1. **Separate objects** for different colors (most reliable).
   - User assigns filament slots in Bambu Studio.
   - No painting required.

2. **Simple face / region coloring** only when a single body must carry multiple colors and the geometry is clean.
   - Keep regions large and simple.
   - Avoid complex gradients or tiny details.

3. **Texture-to-Color Painting** (newer)
   - Converts a textured model’s texture map into multi-color painting automatically.
   - Ideal for logos, artwork, or decorative patterns already present as textures.

4. **Color Mixer / Gradients**
   - Mix 2–3 filaments to create new hues or smooth gradients.
   - Best on near-vertical walls; test first.
   - Recommended starting point: base layer 0.12 mm, mixed layer 0.20 mm (0.4 mm nozzle).

## Non-AMS

- Ignore color entirely.
- Still pack multiple objects into one 3MF so they can be printed together on one plate.

## Practical tips

- Name objects clearly (`logo_base`, `logo_emblem`, `tray`, `plug`).
- For multi-color logos, keep the raised emblem as a separate object when the design allows.
- Always tell the user which objects should receive which color when you have a recommendation.
- For complex multi-color projects, consider multi-plate organization so different color groups can be managed cleanly.
