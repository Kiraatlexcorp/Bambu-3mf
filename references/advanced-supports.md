# Advanced Support Settings

## Decision Tree

1. Can the part be oriented so it needs no supports? → Do that first.
2. Large flat overhangs → Prefer **Normal** or **Hybrid**.
3. Organic / complex / many small overhangs → Prefer **Tree (Organic)**.
4. Need absolute control → Use **Manual** + Support Painting.

## Key Settings (ranked by impact)

### 1. Support Type
- **Tree (Organic)** — default recommendation for most parts
- **Normal** — best surface on large flat ceilings
- **Hybrid** — automatic mix
- **Manual** — full control via painting

### 2. Threshold Angle
- Default: 30°
- 40–45° → fewer supports
- 20–25° → more aggressive (PETG, TPU, critical overhangs)

### 3. Top Z Distance (most important for clean removal)
- PLA: 0.20–0.25 mm
- PETG: 0.25–0.30 mm
- Rule of thumb: ~1.0–1.25 × layer height
- Smaller = better surface, harder removal
- Larger = easier removal, slightly worse surface

### 4. Interface Layers
- Top Interface Layers: 2 (easy removal) or 3 (better surface)
- Interface Pattern: Concentric (easier removal) or Rectilinear (stronger)
- Top Interface Spacing: 0.5 mm default

### 5. Other Useful Options
- Support on build plate only → cleaner parts, longer branches
- Remove small overhangs → reduces unnecessary supports
- Support critical regions only (Tree) → more conservative

## Recommended Starting Profiles

**Easy Removal (PLA functional parts)**
```
Type: Tree (Organic)
Threshold: 35–40°
Top Z Distance: 0.22–0.25 mm
Top Interface Layers: 2
Interface Pattern: Concentric
Support on build plate only: On when possible
```

**Best Surface Quality**
```
Type: Normal or Hybrid
Threshold: 30°
Top Z Distance: 0.15–0.20 mm
Top Interface Layers: 3–4
Interface Pattern: Rectilinear
```

## Support Painting
- Left click = Enforcer
- Right click = Blocker
- Shift + Left = Erase
- Alt/Ctrl + Scroll = Brush size
- Right-click model → Add Support Enforcer / Blocker (primitives)

## Multi-Material Interface (AMS)
Assign a dedicated support filament to the **interface** only.
When using real support material, Top Z Distance can be set to 0.
