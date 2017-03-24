# The All-Seeing Pi

In this resource, you will make a tweeting touchscreen photo booth using a Raspberry Pi.

## Making the photo booth housing
You can create your All-Seeing Pi using any housing you like. Our first iteration used a humble cardboard box, but you might want to create a masterpiece of carpentry or laser-cutting wizardry to hold your All-Seeing Pi.

  ![All-Seeing Pi in a cardboard box](images/asp-cardboard.png)

If you don't have fancy buttons or a touchscreen, that's OK too: you can still make the All-Seeing Pi! Here is a picture of the setup we used when creating this resource: the only extra hardware requirements are two tactile push buttons, four jumper leads, a breadboard, and a Camera Module. You can use your usual monitor, keyboard, and mouse.

  ![All Seeing Pi test setup](images/test-setup.png)

## Connecting the Raspberry Pi touchscreen

1. Set up your Raspberry Pi touchscreen. There is a [good tutorial](https://thepihut.com/blogs/raspberry-pi-tutorials/45295044-raspberry-pi-7-touch-screen-assembly-guide) available to help you. Ensure that you power the touchscreen via the Raspberry Pi with jumper leads as shown in the tutorial, and that the power supply you use is a good quality one.

1. Situate your screen within the housing of your choice, ensuring you can still access the Raspberry Pi.

## Connecting the Camera Module

1. Connect the Camera Module to the Raspberry Pi with the blue side of the connector facing the USB ports:

  ![Connect the camera](images/connect-camera.png)

1. Situate the Camera Module in your chosen housing. If you are using glue to secure it in place, be careful not to get any glue onto the connectors or camera components or they may stop working.

## Connecting the buttons

1. Using jumper leads, wire one button to **GPIO 23** and any ground pin, and the other button to **GPIO 25** and any ground pin.

1. Situate the buttons in your chosen housing. In the software, the button connected to GPIO 23 will select the next overlay, and the button connected to GPIO 25 will take the picture. (Don't worry if you accidentally wire your buttons up the other way around: you can simply swap the pin numbers in the code!)

    ![All-Seeing Pi in a laser-cut box](images/asp-lasercut.png)

## Finishing the setup

1. To write the software, you will also need to connect a keyboard and mouse to your Raspberry Pi, as well as a display if you are not using the touchscreen.

1. Power your Raspberry Pi on and, if you are using one, check that the touchscreen works.

Once you have set up your hardware, head over to [worksheet 2](worksheet2.md) to find out how to write the software to control your All-Seeing Pi.
