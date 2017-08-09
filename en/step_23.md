## Remove all overlays

This function iterates over all overlays attached to the `camera` object, and removes them.

```python
def remove_overlays(camera):

    # Remove all overlays from the camera preview
    for o in camera.overlays:
        camera.remove_overlay(o)
```

