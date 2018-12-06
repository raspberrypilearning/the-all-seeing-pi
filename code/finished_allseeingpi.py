from picamera import PiCamera
from gpiozero import Button
from overlay_functions import *
from time import gmtime, strftime
from guizero import App, PushButton, Text, Picture
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# Tell the next overlay button what to do
def next_overlay():
    global overlay
    overlay = next(all_overlays)
    preview_overlay(camera, overlay)

# Tell the take picture button what to do
def take_picture():
    global output
    output = strftime("/home/pi/allseeingpi/image-%d-%m %H:%M.png", gmtime())
    camera.capture(output)
    camera.stop_preview()
    remove_overlays(camera)
    output_overlay(output, overlay)

    # Save a smaller gif
    size = 400, 400
    gif_img = Image.open(output)
    gif_img.thumbnail(size, Image.ANTIALIAS)
    gif_img.save(latest_photo, 'gif')

    # Set the gui picture to this picture
    your_pic.set(latest_photo)


def new_picture():
    camera.start_preview(alpha=128)
    preview_overlay(camera, overlay)


def send_tweet():
    twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )

    # Send the tweet
    message = "The All Seeing Pi saw you!"
    with open(output, 'rb') as photo:
        twitter.update_status_with_media(status=message, media=photo)

# Set up buttons
next_overlay_btn = Button(23)
next_overlay_btn.when_pressed = next_overlay
take_pic_btn = Button(25)
take_pic_btn.when_pressed = take_picture

# Set up camera (with resolution of the touchscreen)
camera = PiCamera()
camera.resolution = (1024, 768)
camera.hflip = True

# Start camera preview
camera.start_preview(alpha=128)

# Set up filename
output = ""

latest_photo = '/home/pi/allseeingpi/latest.gif'

app = App("The All Seeing Pi", 800, 480)
#app.tk.attributes("-fullscreen", True)
message = Text(app, "I spotted you!")
your_pic = Picture(app, latest_photo)
new_pic = PushButton(app, new_picture, text="New picture")
tweet_pic = PushButton(app, send_tweet, text="Tweet picture")
app.display()
