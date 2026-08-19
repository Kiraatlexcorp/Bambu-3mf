# Slicer Profiles in Bambu Studio

Bambu Studio uses three profile types. Understanding them (and inheritance) is essential for consistent results.

## The Three Profile Types

| Type | Controls | Examples |
|------|----------|----------|
| **Printer** | Hardware limits, build volume, nozzle, max speeds, start/end G-code | Bambu Lab A1 0.4 nozzle, X1C 0.6 nozzle |
| **Filament** | Temperatures, flow, cooling, retraction, max volumetric speed, pressure advance | Bambu PLA Basic, Generic PETG, custom brand profiles |
| **Process** | Layer height, walls, infill, supports, speeds, quality vs strength | 0.20mm Standard, 0.12mm Fine, 0.20mm Strength |

Select one of each before slicing.

## System vs User Presets

- **System presets** — Built-in by Bambu. Cannot be edited directly. Updated with Studio.
- **User presets** — Your copies/modifications. Can sync to Bambu Cloud.

**Rule:** Never edit a system preset. Always clone → rename → modify → save as User Preset.

## Inheritance

Profiles inherit from parents and only store differences:

```
Generic PLA
  └── Bambu PLA Basic @base
        └── Bambu PLA Basic @BBL X1C
              └── Bambu PLA Basic @BBL X1C 0.2 nozzle
```

When creating custom profiles, start from the closest system/generic profile so you inherit good defaults.

## Creating Good Custom Profiles

### Filament (most common)
1. Find closest system/generic profile (Generic PLA, Generic PETG…).
2. Clone it.
3. Rename clearly: `Brand Material @Printer` (e.g. `Sunlu PLA+ @A1`).
4. Adjust critical values first: nozzle temp, bed temp, max volumetric speed, flow ratio, retraction.
5. Calibrate (Flow Rate → Flow Dynamics).
6. Save as User Preset.

### Process
Useful custom process profiles to create:
- `0.16mm High Quality + Ironing`
- `0.20mm Strength (4 walls, 30%+)`
- `0.12mm Logo / Text`
- `0.20mm PETG Functional`
- `Easy Removal Supports` (higher Top Z + fewer interface layers)

### Printer
Only needed for non-standard nozzles, third-party hotends, or heavily modified machines.

## Project vs User Presets

- **User Preset** — available in all projects, can sync to cloud.
- **Project Preset** — saved only inside the current 3MF (good for experiments).

## Cloud Limits

When sync is enabled:
- ~20 printer presets
- ~100 process presets
- ~200 filament presets

## Guidance for this skill

- Assume standard system profiles unless the user specifies otherwise.
- When recommendations deviate significantly from stock (custom supports, strength, etc.), suggest the user create a matching User Process preset.
- Prefer clear naming so recommendations can easily become permanent User Presets later.
