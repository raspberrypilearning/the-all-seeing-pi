## Put the overlay on the camera preview

This function is passed a `PiCamera` object (`camera`) and a string (`overlay`). It removes all overlays currently associated with the camera object, creates a PIL Image object of the chosen overlay called `overlay_img`, pads that image to display correctly and then adds it to the camera preview. The alpha of the preview is set to 128 so that the overlay is semi transparent. If the overlay was made fully opaque it would obscure the camera preview.

```python
def preview_overlay(camera=None, overlay=None):

    # Remove all overlays
    remove_overlays(camera)

    # Get an Image object of the chosen overlay
    overlay_img = _get_overlay_image(overlay)

    # Pad it to the right resolution
    pad = Image.new('RGB', _pad(camera.resolution))
    pad.paste(overlay_img, (0, 0))

    # Add the overlay
    camera.add_overlay(pad.tobytes(), alpha=128, layer=3)
```

