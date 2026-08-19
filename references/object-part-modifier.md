# Object / Part / Modifier Level Control

Bambu Studio lets you override process settings at three levels. Use the lowest level that achieves the goal.

## Levels

| Level | Scope | When to use |
|-------|-------|-------------|
| **Global** | Entire project | Default settings for most objects |
| **Object** | One complete model | Different settings for different models on the same plate |
| **Part** | Single body inside a multi-body object | Different walls/infill on one body of an assembly |
| **Modifier** | Local region (mesh) | Higher infill only in stress zones, local supports, etc. |

Object and Part settings override Global. Modifiers override everything in their volume.

## Practical Examples

- **Strength where it matters**  
  Keep global 15% infill, add a modifier with 40% infill + 4 walls only around screw bosses or load paths.

- **Clean logo / text**  
  Object-level lower layer height or ironing only on the logo plaque.

- **Mixed materials feel**  
  Different wall counts or top surface patterns on different parts of the same multi-body object.

- **Local supports**  
  Use a modifier or support painting so only critical overhangs get supports.

## Workflow Tips

1. Set good Global defaults first.
2. Only go to Object/Part level when one model truly needs different settings.
3. Use modifiers sparingly — they are powerful but make the project harder to maintain.
4. Name objects clearly in the 3MF so the user can easily find them later in Bambu Studio.

## 3MF Considerations

When exporting multi-object 3MFs:
- Keep logical separation of objects (tray, logo, plugs, etc.).
- Clear object names make Object-level overrides easy for the user.
- Do not flatten everything into a single body unless necessary.
