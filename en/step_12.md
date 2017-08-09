## Change overlays with a button

- The other button you wired up to your All-Seeing Pi (called `next_overlay_btn`) will be the one we use to switch between the various overlays. Locate the function `def next_overlay():` and delete the indented line `print ("Next overlay")`. In its place, add the following code, making sure the lines are indented to show that they are part of the function:

    ```python
    def next_overlay():
        global overlay
        overlay = next(all_overlays)
        preview_overlay(camera, overlay)
    ```

    First, we have to declare that we want to use the global variable, `overlay`. This means that when we change the overlay, that value is saved so that we can access it and use it from anywhere, and the change isn't lost when we exit this function.

    The second line gets the next overlay from the list of `all_overlays` (defined within the `overlay_functions.py` file), and sets this as the current `overlay`. Then, the function `preview_overlay()` is called to display the new overlay.

- Save your program, and run it by pressing **F5**. Check that when you press the button to change between overlays, the overlays change. Ensure you have at least one overlay image in your overlays folder to be able to change between them!

    Here is the [program so far](resources/change_overlays_and_take_picture.py) if you want to check your progress.

- You will notice that, when you take a picture, two things happen. Firstly, the overlay does not disappear and probably makes it quite difficult to see what you are doing: close the Python shell window to get rid of the overlay. Secondly, people can see a camera preview and can choose a silly hat from the overlays, but, when they take the photograph, the overlay disappears. We need to add code to remove the overlay from the screen once the picture is taken, and superimpose it onto the saved photograph.

