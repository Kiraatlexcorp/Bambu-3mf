# Hidden Quality Tools

These tools separate good prints from great ones. Most users never touch them.

## Seam Painting

The Z-seam is the vertical line where each outer wall starts/stops.  
Automatic placement is often visible on the “front” of a part.

**When to use**
- Boxes, cases, logos, any part with a preferred viewing face
- Functional parts where a seam on a critical surface is undesirable

**How**
Right-click model → Seam painting. Paint the preferred seam locations (or block bad ones).

## Variable Layer Height

Lets you use finer layers only where they matter (curves, shallow slopes, text) while keeping the rest of the model at a faster layer height.

**When to use**
- Organic shapes, fillets, shallow overhangs, detailed logos
- Any model where 0.08/0.12 mm everywhere would be too slow

**How**
Use the Variable Layer Height tool (slider + adaptive or manual painting).

## Counterbore Hole Bridging (Quality → Advanced)

New optimisation specifically for the circular top surface of counterbore / countersunk holes.

Enable when the model has recessed holes for bolt heads or heat-set inserts. Produces cleaner bridges and better seating surfaces without supports.

## Fuzzy Skin Painting

Apply fuzzy (textured) skin only to selected areas instead of the whole object. Useful for grip surfaces or hiding layer lines on specific faces.
