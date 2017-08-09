## Set up the camera

- Now that we know the buttons work, let's set up the code for the camera. First add an import statement to the existing ones at the top of the program:

    ```python
    from picamera import PiCamera
    ```

- Locate the existing line `take_pic_btn.when_pressed = take_picture` and, below it, add the following code to set up the camera object:

    ```python
    camera = PiCamera()
    camera.resolution = (800, 480)
    camera.hflip = True
    camera.start_preview(alpha=128)
    ```

This code creates a 'PiCamera' object with the resolution set to 800 × 480, which is the resolution of the Raspberry Pi touchscreen. We also tell the camera to flip the preview horizontally (`hflip`): if we don't do this, the preview image will be mirrored, which makes it hard for people to align themselves with the overlays! We then start the preview with alpha set to `128` so that it is semi-transparent; this is in case we get an error and need to see what is happening underneath. When you are confident that your code works, you can remove the `alpha=128` to make the preview fully opaque.


