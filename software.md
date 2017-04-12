# Software Installation
This resource requires a number of additional software libraries. You will need to be connected to the internet to install these extra libraries.

To install the software you need, run the following commands in a terminal window:

```bash
sudo apt-get install -y python3-picamera python3-pip
sudo pip3 install guizero
sudo pip3 install twython
sudo apt-get install -y python3-PIL
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
