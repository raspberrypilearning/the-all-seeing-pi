## Create a GUI

We have an almost-working All-Seeing Pi. However, when a picture is taken, the camera preview disappears and the user is left staring at the Python shell and the Raspbian desktop. You probably don't want your selfie-takers to have to restart the Python program every time someone takes a picture. We will create a very simple GUI to display the picture that was taken and allow them to take another picture.

- To create the GUI we will use a library called **guizero**, which you should have already installed in the [software installation](software.md) step. Add another import line with the others at the start of your program to bring in the guizero functions we need:

    ```python
    from guizero import App, PushButton, Text, Picture
    ```

- At the bottom of your current program, create the beginning of your GUI.

    ```python
    app = App("The All-Seeing Pi", 800, 480)
    message = Text(app, "I spotted you!")
    app.display()
    ```

    First, we create an **app**, which is the basic container for the GUI. The dimensions are 800 × 480 because that is the resolution of the touchscreen, and the title bar will contain the text "The All-Seeing Pi". It is possible to make the GUI full-screen, but we will not do this for now because it can be difficult for testing. We also create a message, `"I spotted you!"`, and add it to the app before displaying everything.

- Save and run your program again. Check that, when you press the button to take the photo, the camera preview exits and you see a mostly blank GUI with a message saying "I spotted you!".

- Now, between the message line and the `app.display()` line, add another line of code to create a button.

    ```python
    new_pic = PushButton(app, new_picture, text="New picture")
    ```

    Examining the arguments passed to this `PushButton` object, we have three parts:
    
    - `app`: tells the button to add itself to the app
    - `new_picture`: this is the **command**. When the button is pushed, it will call the function `new_picture()` (which we haven't written yet!)
    - `text="New picture"`: this is the text which will appear on the button

- Now write the `new_picture` function so that the button knows what to do when it is pressed. Write this code after the `take_picture()` function, but before the code where we set up the buttons. **Ensure that your cursor is not indented**, otherwise the code you write now will become part of the `take_picture()` function, which we do not want.

    ```python
    def new_picture():
        camera.start_preview(alpha=128)
        preview_overlay(camera, overlay)
    ```

    This function is very straightforward: it simply tells the camera to restart the preview, and to display the overlay (which will be the last overlay we used).

- Save your program, and run it using **F5** once again. Check that you can press your physical button to take a picture, and that the GUI displays once the camera preview disappears. Check that you can press the on-screen button to restart the camera preview and take another picture.

