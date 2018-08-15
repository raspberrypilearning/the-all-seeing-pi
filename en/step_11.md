## Working with overlays

- The All-Seeing Pi is no ordinary photo booth! The second button we set up, `next_overlay_btn`, is used to change between 'overlays': these are fun pictures such as hats, beards, and glasses which appear on the screen as if you are wearing them. Here is an example of a picture taken with an overlay:

    ![Rik with pigtail overlay](images/rik-picture.png)

    You can make your own overlays, or use the ready-made ones we have provided for you to download. If you are creating your own overlays, make sure that they are saved at 800 × 480 resolution as PNG files, with the background set to transparent.

- Create a subfolder called `overlays` within your `allseeingpi` folder, and place your overlay images inside it.

- Navigate to the [overlays folder](https://github.com/raspberrypilearning/the-all-seeing-pi/tree/master/en/resources) of the GitHub repo for this project. Click on the filename of the overlay you would like to use, then right-click on the download link and save the image into the `overlays` folder you just created. Repeat this process until you have saved all of the overlays you would like to use.

- Now [right-click here](resources/overlay_functions.py) and save this file as `overlay_functions.py`. Make sure you save this file in your `allseeingpi` directory (where the `allseeingpi.py` script is also saved). 

- In the `overlay_functions.py` file, find this comment:

    ```
    # EDIT THESE VALUES ------------------------
    ```

    You will need to change this code to specify two things:
    
      - Set the `overlays_dir` to the directory where your overlays are stored. If you are following this tutorial exactly, you will **not** need to change this directory location.
      - Set the `overlays` to be a list of the filenames of the overlays (without extension), surrounded by quotes and separated by commas. For example, if you had overlay images called `rock.png`, `paper.png`, and `scissors.png`, your line of code would look like this:

    ```python
    overlays = ['rock', 'paper', 'scissors']
    ```

- Now go back to your `allseeingpi.py` program. Underneath the other import statements in your program, add another one to import this file:

    ```python
    from overlay_functions import *
    ```

  This will allow us to use all of the overlay functions defined in the `overlay_functions.py` file from within our `allseeingpi.py` file.

