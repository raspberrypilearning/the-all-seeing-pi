## The All Seeing Pi (Overlay Functions)

The following section is for more advanced learners as it explains in detail what the code and functions inside `overlay_functions.py` do. It is possible to make the All Seeing Pi without understanding what these functions do - simply save a copy of the file [overlay_functions.py](resources/overlay_functions.py) into the folder with your code and they will be available.

### Importing necessary libraries

These statements import functions from the `PIL` library to process and save the images and the `itertools` library so that we can cycle through the overlays.

```python
  from PIL import Image
  from itertools import cycle
```

### Setting up the variables

This part sets up the directory where the overlays are saved, and the names of the various overlays. The overlay variable is initialised with the first value in the list.

```python
# EDIT THESE VALUES ------------------------
overlays_dir = "/home/pi/allseeingpi/overlays"
overlays = ['girl', 'cowboy', 'top', 'pink', 'glassesnose', 'moustache', 'sunglasses', 'elvis', 'emo', 'blackhat', 'emo2', 'baseball', 'flowers', 'santa', 'alps', 'mop', 'glasses']
# ------------------------------------------
overlay = overlays[0] # Starting value
```

### Get the overlay as a PIL Image

This function is only used within other functions in this file. Given the name of an overlay as a string, it creates a PIL Image object of that overlay and returns it.

```python
def _get_overlay_image(overlay):

    # Open the overlay as an Image object
    return Image.open(overlays_dir + "/" + overlay + ".png")
```

### Pad the overlay

This function ensures that the overlay is padded correctly so it can be displayed on the preview.

```python
def _pad(resolution, width=32, height=16):
    # Pads the specified resolution
    # up to the nearest multiple of *width* and *height*; this is
    # needed because overlays require padding to the camera's
    # block size (32x16)
    return (
        ((resolution[0] + (width - 1)) // width) * width,
        ((resolution[1] + (height - 1)) // height) * height,
    )
```

### Remove all overlays

This function iterates over all overlays attached to the `camera` object, and removes them.

```python
def remove_overlays(camera):

    # Remove all overlays from the camera preview
    for o in camera.overlays:
        camera.remove_overlay(o)
```

### Put the overlay on the camera preview

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

### Save picture with overlay

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

### Overlays cycle

This code creates a `cycle`. We use the `next()` function on this cycle when the `next_overlay_btn` is pressed in order to receive the next overlay in the list. A cycle is needed because when the end of the list of overlays is reached, we want to automatically begin again with the first overlay.

```python
all_overlays = cycle(overlays)
```

