## What you will need

### Hardware

* Raspberry Pi Camera Module
* Raspberry Pi touchscreen display or standard monitor
* 2 x tactile push buttons
* Breadboard
* 4 x Male-female jumper leads
* 2 x large buttons (optional, to replace tactile push buttons)

### Software

#### Software Installation
This resource requires a number of additional software libraries. You will need to be connected to the internet to install these extra libraries.

To install the software you need, run the following commands in a terminal window:

```bash
sudo pip3 install guizero
sudo pip3 install twython
```

This will install the necessary software to control the Camera Module, create a GUI, and tweet and manipulate images.

If you are using the Raspberry Pi touchscreen to make this resource, you will also need to enter the following commands:

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo apt-get install -y raspberrypi-ui-mods
sudo apt-get install -y raspberrypi-net-mods
```
