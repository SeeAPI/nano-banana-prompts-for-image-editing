# P25 · Remove Unwanted Objects

## 🖼️ Preview

| Before | After |
| :---: | :---: |
| <a href="../assets/remove-object/before.png"><img src="../assets/remove-object/before.png" width="320" height="320" alt="Original image"></a><br>Photo | <a href="../assets/remove-object/after.png"><img src="../assets/remove-object/after.png" width="320" height="320" alt="Removed person"></a> |

## 👇 Workflow

`Photo + target object → object removal`

## 📝 Full Prompt

```text
Remove [object_to_remove] from the uploaded image, including its associated cast shadow and reflection only where they belong to that object. Reconstruct the revealed background seamlessly using the surrounding scene's texture, geometry, perspective, lighting, and depth of field.

Preserve every other person, object, edge, and architectural feature. Do not replace the removed object with anything new, shift nearby subjects, crop the image, or alter overall colors. Avoid smears, repeating texture patterns, blurred patches, and visible edit boundaries. Output one natural-looking image with the original dimensions and framing.
```

<sub>Prompt by SeeAPI</sub>
