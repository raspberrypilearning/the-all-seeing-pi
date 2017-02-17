# The All Seeing Pi (Part 2 - Software)

In this resource you will make a tweeting touch screen photo booth using a Raspberry Pi.

## Test the buttons

1. With the hardware set up, we can begin to program the software that will make everything work. To begin, open the file explorer, then right click on a blank space inside the file explorer window.

  ![File Explorer](images/file-explorer.png)

1. Select `Create new` and then click `Folder`

  ![Create folder menu](images/create-folder.png)

1. Type in the name of the folder where you will store the code and the photographs. We chose to call ours `allseeingpi`. Make a note of the path to this folder which is displayed in the bar at the top, which should be `/home/pi/allseeingpi`

1. From the "Programming" menu, open up "Python 3"

  ![Open Python 3](images/python3-app-menu.png)

1. Create a new Python file by clicking on `File` > `New File`.

1. Click on `File` > `Save` and save your file into the `allseeingpi` folder you just created, with the filename `allseeingpi.py`.

1. We will need the `gpiozero` library. At the start of your Python file add an import statement:

  ```python
  from gpiozero import Button
  ```

1. Next we will set up the buttons. On the [previous worksheet](worksheet.md) we wired our buttons to pins 23 and 25. Let's go ahead and set both buttons up.

  ```python
  next_overlay_btn = Button(23)
  take_pic_btn = Button(25)
  ```

1. Now we will use gpiozero to tell the buttons what to do when pressed. In the code below, `next_overlay` and `take_picture` are functions which will be called when the corresponding button is pressed:

  ```python
    next_overlay_btn.when_pressed = next_overlay
    take_pic_btn.when_pressed = take_picture
  ```

1. We will write these two functions so that the buttons know what to do when they are pressed. Functions are usually written at the start of a program immediately after the `import` statements. Add the functions, but with some placeholder code to just print a message when they are pressed, so we can test them.

  ```python
  def next_overlay():
    print("Next overlay")

  def take_picture():
    print("Take a picture")
  ```

1. Press `F5`, save and run your program. Try pressing each button and check that a different message pops up for each in the Python shell.

    ![Test the buttons](images/test-buttons.png)

# Set up the camera

1. Now that we know the buttons work, let's set up the camera. First add an import statement with the others at the top:

  ```python
  from picamera import PiCamera
  ```

1. Locate the existing line `take_pic_btn.when_pressed = take_picture` and below it add the following code to set up the camera object:

  ```python
  camera = PiCamera()
  camera.resolution = (800, 480)
  camera.hflip = True
  camera.start_preview(alpha=128)
  ```

  This code creates a PiCamera object with the resolution set to 800x480 which is the resolution of the Raspberry Pi touchscreen. We also tell the camera to flip the preview horizontally (`hflip`) because otherwise the preview image will be mirrored and this makes it hard for people to align themselves with the overlays! We then start the preview with alpha set to `128` so that it is semi-transparent in case we get an error and need to see what is happening underneath. When you are confident your code works you can remove the `alpha=128` to make the preview fully opaque.


## Take a picture when the button is pressed

1. Since we will probably take lots of pictures with the All Seeing Pi, we will put the date and time the picture was taken within the filename to avoid a picture being overwritten each time a new one is taken. To do this, we will need the `gmtime` and `strftime` functions from the time library, so add this line with the other `import` statements:

  ```python
  from time import gmtime, strftime
  ```

1. Underneath your camera set up code, add the following line:

  ```python
  output = strftime("/home/pi/allseeingpi/image-%d-%m %H:%M.png", gmtime())
  ```

  This will create a variable called `output` which contains the location and filename of where the captured photo will be saved. The `%d`, `%m` (etc) characters are how we specify the time format - `%d` means the day and `%m` means the month, for example. If you would like the date format in your filename to be different, there is a full [strftime reference](https://docs.python.org/2/library/time.html#time.strftime) available. The current date and time is provided by calling the function `gmtime()`.

1. Now we will add some proper code to the `take_picture()` function, so that it actually takes a picture instead of just printing a message. Locate the line `def take_picture()`. Delete the line `print("Take a picture")` and in its place, add the following lines, making sure they are indented:

  ```python
  def take_picture():
    camera.capture(output)
    camera.stop_preview()
  ```

  This code captures a picture, saving it to the location we just defined in the variable `output`. It then stops the camera preview.

1. Navigate to the folder `/home/pi/allseeingpi` and check that the picture you just took has saved correctly.

## Working with overlays

1. The All Seeing Pi is no ordinary photo booth! The second button we set up, `next_overlay_btn`, is used to change between 'overlays' - fun pictures such as hats, beards and glasses which appear on the screen as if you are wearing them. Here is an example of a picture taken with an overlay:

    ![Rik with pigtail overlay](images/rik-picture.png)

    You can make your own overlays or we have provided some ready made ones that you can download in the [overlays folder](https://github.com/raspberrypilearning/the-all-seeing-pi) of the GitHub repo for this project. If you are creating your own overlays, make sure that they are saved at 800x480 resolution as PNG files, with the background set to transparent.

1. Create a subfolder within your `allseeingpi` folder called `overlays` and place your overlay images inside it.

1. We will need some functions to be able to work with our overlays. If you would like to use our [pre-written overlay functions](code/overlay_functions.py), download a copy of the file and save it as `overlay_functions.py` in your `allseeingpi` directory. If you would like to see a full explanation of what these functions do, or you would prefer to write them yourself, head to the [overlay functions explanation page](worksheet3.md) to find out how to do this.

1. Next to the other `import` statements in your program, add another one to import this file:

  ```python
  from overlay_functions import *
  ```

  This will allow us to use all of the overlay functions defined in the `overlay_functions.py` file, from within our `allseeingpi.py` file.

## Change overlays with a button

1. The other button you wired up to your All Seeing Pi (called `next_overlay_btn`) will be the one we use to switch between the various overlays. Locate the `def next_overlay():` line and delete the line `print ("Next overlay")`. In its place, add the following code, making sure the lines are indented:

  ```python
  overlay = next(all_overlays)
  preview_overlay(camera, overlay)
  ```

  The first line gets the *next overlay* from the list of `all_overlays` which is defined within the `overlay_functions.py` file. Then, the function `preview_overlay()` is called to add the overlay by giving it both the camera object and the overlay we want.

1. Save your program and run it by pressing `F5`. Check that when you press the button to change between overlays, the overlays change. (Ensure you have at least one overlay image in your overlays folder!)


## Save overlay on your picture

## Tweet picture

## Create a GUI
