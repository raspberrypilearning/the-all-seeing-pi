## Save picture with overlay

This function takes the location of the photograph (`output`) and the given overlay (`overlay`), both as strings. It then creates a PIL Image object of the specified overlay, also creates a blank PIL Image to save the finished output to, and then combines the photograph with the overlay, re-saving the finished photograph at the `output` location.

```python
def output_overlay(output=None, overlay=None):

    # Take an overlay Image
    overlay_img = _get_overlay_image(overlay)

    # ...and a captured photo
    output_img = Image.open(output).convert('RGBA')

    # Combine the two and save the image as output
    new_output = Image.alpha_composite(output_img, overlay_img)
    new_output.save(output)
```

