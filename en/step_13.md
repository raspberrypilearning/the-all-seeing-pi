## Save an overlay on your picture

- Locate the function `def take_picture():` and add two lines of code at the end of the function:

    ```python
    def take_picture():
        camera.capture(output)
        camera.stop_preview()
        remove_overlays(camera)         # Add this line
        output_overlay(output, overlay) # Add this line
    ```

    Here we are using two more functions from the `overlay_functions` file. The function `remove_overlays` does exactly what it says, and removes all of the overlays so they don't hang around after we take a photograph. The `output_overlay` function takes the photograph and the overlay and glues them together so the resulting final output is a photograph with the chosen overlay superimposed.

- Once again, save your file and run it using **F5** to check that you can now change between overlays, and that, when you take a photograph, your chosen overlay is saved as part of the picture.

