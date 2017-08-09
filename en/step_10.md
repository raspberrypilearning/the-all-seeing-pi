## Take a picture when the button is pressed

- Since we will probably take lots of pictures with the All-Seeing Pi, we will put the date and time at which the picture was taken within the filename to avoid a picture being overwritten each time a new one is taken. To do this, we will need the `gmtime` and `strftime` functions from the `time` library, so add this line to the other import statements:

    ```python
    from time import gmtime, strftime
    ```

- Underneath the code to set up the camera, add the following line:

    ```python
    output = strftime("/home/pi/allseeingpi/image-%d-%m %H:%M.png", gmtime())
    ```

    This will create a variable called `output` which contains the location and filename of where the captured photo will be saved. The `%d`, `%m` (etc) characters are how we specify the time format: `%d` means the day and `%m` means the month, for example. If you would like the date format in your filename to be different, there is a full [reference guide](https://docs.python.org/2/library/time.html#time.strftime) to `strftime` available. The current date and time is provided by calling the function `gmtime()`.

- Now let's revisit the `take_picture()` function and add some new code so that it actually takes a picture instead of just printing a message. Locate the line `def take_picture()`. Delete the line `print("Take a picture")` and in its place, add the following lines, making sure they are indented:

    ```python
    def take_picture():
        camera.capture(output)
        camera.stop_preview()
    ```

    This code captures a picture, saving it to the location we just defined in the variable `output`. It then stops the camera preview.

- Press **F5** to run your program, then press the button to take a picture.

- Navigate to the folder `/home/pi/allseeingpi` and check that the picture you just took has saved correctly.

