# Custom G-code & “Macros” in Bambu Studio

Bambu Studio does not have Klipper-style named macros.  
What people call “macros” are **custom G-code slots** + **placeholders** + **per-layer custom G-code**.

## Available Custom G-code Slots

| Slot | Location | When it runs | Common use |
|------|----------|--------------|------------|
| Machine Start G-code | Printer → Machine G-code | Start of every print | Homing, purge, initial temps |
| Machine End G-code | Printer → Machine G-code | End of every print | Present filament, cool down, park |
| Filament Start G-code | Filament settings | First use of a filament | Temp, pressure advance |
| Filament End G-code | Filament settings | When a filament finishes | Retract / cool |
| Change Filament G-code | Printer → Machine G-code | Every tool change | Unload / load / purge (most powerful) |
| Layer Change G-code | Printer → Machine G-code | Start of every new layer | Rarely used |
| Pause G-code | Printer → Machine G-code | When pause is triggered | Custom park + message |
| Per-layer Custom G-code | Preview tab (right-click layer) | Specific layer | Temp towers, speed changes, magnet pauses |

## Placeholders (variables)

All process/filament/printer parameters can be used as placeholders.  
Official list: https://wiki.bambulab.com/en/software/bambu-studio/placeholder-list

Most useful:

```
{layer_num}
{layer_z}
{max_layer_z}
{current_extruder}
{previous_extruder}
{next_extruder}
{filament_type[current_extruder]}
{nozzle_temperature[current_extruder]}
{old_filament_temp}
{new_filament_temp}
{flush_length_1} … {flush_length_16}
```

Conditionals are supported:

```
{if layer_num == 10}
M104 S250
{endif}

{if filament_type[next_extruder] == "PETG"}
; special PETG handling
{endif}
```

## Per-layer Custom G-code (easiest method)

1. Slice the model
2. Go to Preview tab
3. Move layer slider to desired layer
4. Right-click the layer bar → **Add custom G-code** (or Add Pause / Add Filament Change)

Common uses:
- Temperature towers
- Speed changes at a certain height (`M220 S120`)
- Pause to insert magnets (`M400 U1`)
- Fan speed changes

## Practical Recipes

**Pause for magnets / inserts**
```
M400 U1          ; pause and wait for user
```

**Raise temperature at a specific layer**
```
M104 S250
```

**Change speed (Sports mode example)**
```
M220 S125        ; 125% speed
```

**No final unload (keep filament loaded)**
Many users delete or comment out the final AMS unload section in Machine End G-code so the next print starts faster.

## Recommendations for this skill

- When generating 3MFs, do **not** embed complex custom G-code unless the user explicitly requests it.
- If the user asks for temperature towers, magnet pauses, or special filament-change behaviour, provide the exact G-code snippet and tell them where to paste it.
- Prefer the per-layer method for one-off changes (safer and easier to remove).
- For permanent behaviour (e.g. better end G-code or no-AMS filament change), guide the user to edit the Printer / Filament preset and save it as a User Preset.
