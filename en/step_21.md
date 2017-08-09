## Get the overlay as a PIL Image

This function is only used within other functions in this file. Given the name of an overlay as a string, it creates a PIL Image object of that overlay and returns it.

```python
def _get_overlay_image(overlay):

    # Open the overlay as an Image object
    return Image.open(overlays_dir + "/" + overlay + ".png")
```

