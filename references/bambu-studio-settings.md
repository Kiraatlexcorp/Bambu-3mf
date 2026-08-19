# Recommended Bambu Studio Settings

Starting points only. Adjust after the first test print.

## General (0.4 mm nozzle)

- Layer height: 0.20 mm (0.12–0.16 mm for fine logos/text)
- Wall loops: 2–3 (3–4 for load-bearing)
- Top/bottom shells: 4–5
- Infill: 15 % gyroid (25–40 % for strength)
- Sparse infill pattern: Gyroid
- Detect thin walls: On
- Ironing: Off (unless top surface is critical)

## Supports

- Prefer designing parts that need no supports.
- When required: Tree supports (auto) or normal supports with 0.2 mm Z distance.
- Support on build plate only when possible.

## Materials

| Material  | First layer | Other layers | Bed   | Notes                      |
|-----------|-------------|--------------|-------|----------------------------|
| PLA       | 220         | 210–215      | 55–60 | Default for most parts     |
| PLA Matte | 220         | 210–215      | 55–60 | Good for logos             |
| PETG      | 250         | 240–245      | 70–80 | Stronger, slightly stringy |
| TPU 95A   | 230–240     | 220–230      | 30–40 | Slow print speed           |

## AMS specific

- Flushing volumes: leave default unless color bleeding is visible.
- For multi-color logos, put the dominant color as the first object when possible.

## Plate arrangement

- Keep parts at least 5–8 mm apart.
- Orient large flat faces down.
- For under-machine trays, print with open top up (bottom on bed).
