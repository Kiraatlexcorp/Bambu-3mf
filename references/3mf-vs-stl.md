# 3MF vs STL for Bambu Lab

## Prefer 3MF when

- User has a Bambu Lab printer
- Multiple parts need to travel together
- AMS color assignment is desired
- Ready-to-slice project is the goal

## Advantages of 3MF

- Native format of Bambu Studio
- Multiple named objects in one file
- Explicit units
- Smaller compressed files
- Can carry plate arrangement and basic project state
- Supports material / color assignment for AMS
- Better precision and metadata

## When STL is still acceptable

- Single solid part with no internal cavities
- Quick one-off transfer to a non-Bambu slicer

## CadQuery export rule

```python
# Preferred — preserves cavities
cq.exporters.export(solid, "part.3mf")
```

Avoid STL→3MF conversion for any part that contains enclosed voids, magnet pockets, or internal channels. CadQuery’s native writer is safer.
