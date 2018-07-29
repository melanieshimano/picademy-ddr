'''

authors: Melanie Shimano and Gerald Smith
date: June 22, 2018
Dance, Dance Revolution Raspberry Pi #Picademy Game + Twitter Bot
Use with Python 3.6, Raspberry Pi B+, Raspberry Pi camera module,
Raspberry Pi Sense HAT, PIR motion sensor

'''

from picamera import PiCamera #for the RPi Camera
from time import sleep #allows us to use the sleep function 
from gpiozero import MotionSensor #for the PIR motion sensor
from sense_hat import SenseHat #for the RPi Sense HAT
import random #to generate random directions for DDR
from os import system
from twython import Twython #to automatically tweet out gifs from DDR 

camera = PiCamera()
sensor = MotionSensor(4)
sense = SenseHat()

#change the camera resolution so that the gifs will upload to Twitter
camera.resolution = (1024, 768)

#motion prompts for user to enter name
sensor.wait_for_motion()
name = input("What's your name?")

#game directions
print ("Welcome to Raspberr Pi DDR" + str(name) + "!")
sleep(3)
print("After the countdown, the LED will prompt you with dancing directions")
sleep(3)
print("Use your hands to point in the direction of arrows")
sleep(3)
print("When you're finished, @Picademy_DDR will tweet out a gif of your epic dance battle on Twitter")
sleep(3.5)
print("Good Luck!")
sleep(3)

#colors for sense hat
l =(255,255,0) #yellow
d= (0,0,156) #dark blue

#sense hat countdown variables
one =[
    d, d, d, l, l, d, d, d,
    d, d, d, l, l, d, d, d,
    d, d, d, l, l, d, d, d,
    d, d, d, l, l, d, d, d,
    d, d, d, l, l, d, d, d,
    d, d, d, l, l, d, d, d,
    d, d, d, l, l, d, d, d,
    d, d, d, l, l, d, d, d
    ]

two =[
    d, d, l, l, l, l, l, d,
    d, d, l, d, d, d, l, d,
    d, d, l, d, d, d, l, d,
    d, d, d, d, d, l, d, d,
    d, d, d, d, l, d, d, d,
    d, d, d, l, d, d, d, d,
    d, d, l, d, d, d, d, d,
    d, d, l, l, l, l, l, d
    ]

three =[
    d, d, l, l, l, l, d, d,
    d, d, d, d, d, l, d, d,
    d, d, d, d, d, l, d, d,
    d, d, d, l, l, l, d, d,
    d, d, d, d, d, l, d, d,
    d, d, d, d, d, l, d, d,
    d, d, d, d, d, l, d, d,
    d, d, l, l, l, l, d, d
    ]

go =[
    d, d, d, d, d, d, d, d,
    d, d, d, d, d, d, d, d,
    l, l, l, l, d, l, l, l,
    l, d, d, d, d, l, d, l,
    l, d, l, l, d, l, d, l,
    l, d, d, l, d, l, d, l,
    l, d, d, l, d, l, d, l,
    l, l, l, l, d, l, l, l
    ]
#set pixels to countdown to camera
sense.set_pixels(three)
sleep(1)
sense.set_pixels(two)
sleep(1)
sense.set_pixels(one)
sleep(1)
sense.set_pixels(go)
sleep(1)

#turn on camera preview
camera.start_preview(alpha=180)

#make variables for 8 different directions
#vertical horiztonal directions

down= [
    d, d, d, d, l, d, d, d,
    d, d, d, d, l, d, d, d,
    d, d, d, d, l, d, d, d, 
    d, d, d, d, l, d, d, d,
    d, d, d, d, l, d, d, d,
    d, d, l, d, l, d, l, d,
    d, d, d, l, l, l, d, d,
    d, d, d, d, l, d, d, d
    ]

up= [
    d, d, d, d, l, d, d, d,
    d, d, d, l, l, l, d, d,
    d, d, l, d, l, d, l, d, 
    d, d, d, d, l, d, d, d,
    d, d, d, d, l, d, d, d,
    d, d, d, d, l, d, d, d,
    d, d, d, d, l, d, d, d,
    d, d, d, d, l, d, d, d
    ]

right=[ 
    d, d, d, d, d, d, d, d,
    d, d, d, d, d, l, d, d,
    d, d, d, d, d, d, l, d, 
    d, d, l, l, l, l, l, l,
    d, d, d, d, d, d, l, d,
    d, d, d, d, d, l, d, d,
    d, d, d, d, d, d, d, d,
    d, d, d, d, d, d, d, d
    ]

left= [ 
    d, d, d, d, d, d, d, d,
    d, d, d, d, d, d, d, d,
    d, d, l, d, d, d, d, d, 
    d, l, d, d, d, d, d, d,
    l, l, l, l, l, l, d, d,
    d, l, d, d, d, d, d, d,
    d, d, l, d, d, d, d, d,
    d, d, d, d, d, d, d, d
    ]

#Diagonal directions

dright=[
    l, d, d, d, d, d, d, d,
    d, l, d, d, d, d, d, d,
    d, d, l, d, d, d, d, d,
    d, d, d, l, d, d, d, d,
    d, d, d, d, l, d, d, l,
    d, d, d, d, d, l, d, l,
    d, d, d, d, d, d, l, l,
    d, d, d, d, l, l, l, l
    ]

uleft =[
    l, l, l, l, d, d, d, d,
    l, l, d, d, d, d, d, d,
    l, d, l, d, d, d, d, d,
    l, d, d, l, d, d, d, d,
    d, d, d, d, l, d, d, d,
    d, d, d, d, d, l, d, d,
    d, d, d, d, d, d, l, d,
    d, d, d, d, d, d, d, l
    ]

dleft=[
    d, d, d, d, d, d, d, l,
    d, d, d, d, d, d, l, d,
    d, d, d, d, d, l, d, d,
    d, d, d, d, l, d, d, d,
    l, d, d, l, d, d, d, d,
    l, d, l, d, d, d, d, d,
    l, l, d, d, d, d, d, d,
    l, l, l, l, d, d, d, d
    ]

uright =[
    d, d, d, d, l, l, l, l,
    d, d, d, d, d, d, l, l,
    d, d, d, d, d, l, d, l,
    d, d, d, d, l, d, d, l,
    d, d, d, l, d, d, d, d,
    d, d, l, d, d, d, d, d,
    d, l, d, d, d, d, d, d,
    l, d, d, d, d, d, d, d
    ]

blank =[
    d, d, d, d, d, d, d, d,
    d, d, d, d, d, d, d, d,
    d, d, d, d, d, d, d, d,
    d, d, d, d, d, d, d, d,
    d, d, d, d, d, d, d, d,
    d, d, d, d, d, d, d, d,
    d, d, d, d, d, d, d, d,
    d, d, d, d, d, d, d, d
    ]


#show five random directions on sense hat
#take photo 0.5 seconds after each direction shows
#show blank screen in between each arrow

#list of direction arrows
arrows = [up, down, left, right, uleft, uright, dleft, dright]

for i in range(5):
    sense.set_pixels(random.choice(arrows))
    sleep(1)
    camera.capture('/home/pi/DDR_Pi{0:04d}.jpg'.format(i))
    sense.set_pixels(blank)
    sleep(0.5)
    
camera.stop_preview()

#make timelapse gif

system ('convert -delay 10 -loop 0 DDR_Pi*.jpg animation.gif')
print('your gif finished...')

#send gif to a tweet

#send to twitter
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#message for the tweet
message = 'Epic dance battle by ' + str(name)
#gif attached to the tweet
gif = open('/home/pi/animation.gif', 'rb')

#upload message and gif to Twitter
response = twitter.upload_media(media=gif)
media_id = [response['media_id']]

twitter.update_status(status=message, media_ids=media_id)
print("Tweeted: %s" % message)





