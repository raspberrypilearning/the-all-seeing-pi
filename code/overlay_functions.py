# Adapted from some original code by bennuttall and waveform80
# -------------------------------------------------------------
 
from PIL import Image
from itertools import cycle

# EDIT THESE VALUES ------------------------
overlays_dir = "/home/pi/allseeingpi/overlays"
overlays = ['girl', 'cowboy', 'top', 'pink', 'glassesnose', 'moustache', 'sunglasses', 'elvis', 'emo', 'blackhat', 'emo2', 'baseball', 'flowers', 'santa', 'alps', 'mop', 'glasses']
# ------------------------------------------


overlay = overlays[0] # Starting value

def _get_overlay_image(overlay):
    
    # Open the overlay as an Image object
    return Image.open(overlays_dir + "/" + overlay + ".png")

def _pad(resolution, width=32, height=16):
    # Pads the specified resolution
    # up to the nearest multiple of *width* and *height*; this is
    # needed because overlays require padding to the camera's
    # block size (32x16)
    return (
        ((resolution[0] + (width - 1)) // width) * width,
        ((resolution[1] + (height - 1)) // height) * height,
    )

def remove_overlays(camera):
    
    # Remove all overlays from the camera preview
    for o in camera.overlays:
        camera.remove_overlay(o) 


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

def output_overlay(output=None, overlay=None):

    # Take an overlay Image
    overlay_img = _get_overlay_image(overlay)

    # ...and a captured photo
    output_img = Image.open(output).convert('RGBA')

    # Combine the two and save the image as output
    new_output = Image.alpha_composite(output_img, overlay_img)
    new_output.save(output)

all_overlays = cycle(overlays)
