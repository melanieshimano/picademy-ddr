# Raspberry Pi Dance, Dance, Revolution + Twitter Bot
Looking for a fun way to learn how to use Raspberry Pi and a variety of Raspberry Pi accessories? In this tutorial, you'll learn how to use a [Raspberry Pi](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/), [Sense HAT](https://www.raspberrypi.org/products/sense-hat/), [PIR (motion) sensor](https://www.adafruit.com/product/189), and a [Raspberry Pi camera](https://www.adafruit.com/product/3099) to make a Dance, Dance, Revolution game that automatically uploads a gif of your dance to Twitter.
 ![Alt text](https://github.com/melanieshimano/picademy-ddr/blob/master/animation.gif)

We created this Raspberry Pi Dance, Dance, Revolution Game at Picademy Jersey City (June 2018). See the final output on Twitter here: https://twitter.com/Picademy_DDR

# Overview
- The motion sensor detects a new player, which prompts the player(s) to input their name(s) and gives directions for the game.
- The Sense HAT displays “3, 2, 1, GO” and then give the player(s) five random directions to point their arms for the dance
- While the player is dancing, the Raspberry Pi camera captures an image of each dance motion, then stitches these together into an animated gif and posts the final gif of the dance to the [Picademy_DDR](https://twitter.com/Picademy_DDR) Twitter account!

![Alt text](https://github.com/melanieshimano/picademy-ddr/blob/master/tutorial_photos/sense_hat_directions_example.gif)

If you want to get a little more familiar with all of the Raspberry Pi accessories before starting, you can look through the following tutorials:

[Raspberry Pi Camera](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera)
[Sense HAT](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat)
[PIR (motion) sensor](https://projects.raspberrypi.org/en/projects/physical-computing/13)

# Materials
- [Raspberry Pi + micro SD card with NOOBS](https://www.amazon.com/ELEMENT-Element14-Raspberry-Pi-Motherboard/dp/B07BDR5PDW/ref=sr_1_3?s=pc&ie=UTF8&qid=1532898659&sr=1-3&keywords=raspberry+pi+3+b%2B) (I used a B+, but you should be able to use any model compatible with the other materials)
- [Sense HAT](https://www.adafruit.com/product/2738)
- [Mini black hat hack3r](https://www.adafruit.com/product/3182)
- [Raspberry Pi compatible camera](https://www.adafruit.com/product/3099)
- [PIR (motion) sensor](https://www.adafruit.com/product/189)
- [Three female-female jumper wires](https://www.adafruit.com/product/266)
- [Raspberry Pi power source](https://www.amazon.com/CanaKit-Raspberry-Supply-Adapter-Listed/dp/B00MARDJZ4/ref=sr_1_3?s=electronics&ie=UTF8&qid=1532898933&sr=1-3&keywords=raspberry+pi+power&smid=A30ZYR2W3VAJ0A)
- Monitor, keyboard, and mouse to work with the Raspberry Pi
- [Mounting putty](https://www.amazon.com/Duck-Reusable-Removable-Mounting-1436912/dp/B000BQMFEC/ref=sr_1_3?ie=UTF8&qid=1532898965&sr=8-3&keywords=mounting+putty) or tape to hold up the camera, motion sensor, and Sense HAT

# Prerequisites 
You’ll need to install the following through the Raspberry Pi terminal:
```
pip install imagemagick
pip install twython
```

# Instructions

1.	Because we need GPIO pins for both the Sense HAT and for the PIR sensor, we’ll attach the mini black hat hack3r to the GPIO pins to extend their functionality. Make sure the ribbon wire connects to the GPIO pins such that it crosses over the body of the Raspberry Pi (RPi) and connects to the row of pins outside of the dotted lines
![Alt text](https://github.com/melanieshimano/picademy-ddr/blob/master/tutorial_photos/rpi_blackhat.jpg)

2.	Connect the Sense HAT to the GPIO pins on the opposite side of the ribbon wire so that you still have access to the middle row of GPIO pins on the mini black hat hack3r
![Alt text](https://github.com/melanieshimano/picademy-ddr/blob/master/tutorial_photos/sense_hat.jpg)

3.	Connect one end of the three jumper wires to the PIR sensor, and connect the other end to the open GPIO pins according to the PIR pin labels that are underneath the removeable Fresnel lens (white cap) on the PIR:

   - PIR Sensor VCC -> RPi 5V (green)
   - PIR Sensor OUT -> RPi any GPIO numbered pin (yellow, on GPIO 4)
   - PIR Sensor GND -> RPi any GPIO GND pin (orange)
![Alt text](https://github.com/melanieshimano/picademy-ddr/blob/master/tutorial_photos/pir_labels.jpg)
![Alt text](https://github.com/melanieshimano/picademy-ddr/blob/master/tutorial_photos/pir_gpio.jpg)
![Alt text](https://github.com/melanieshimano/picademy-ddr/blob/master/tutorial_photos/pir_attached.jpg)

4.	Connect the Raspberry Pi camera to the camera port on the Raspberry Pi such that the blue strip points toward the RPi audio jack
![Alt text](https://github.com/melanieshimano/picademy-ddr/blob/master/tutorial_photos/rpi_camera.jpg)

5.	Set up the RPi setup such that the camera, PIR sensor, and Sense HAT are at eye level—we used mounting putty to stick these on our monitor, but you can get creative and hold these up in any way that best fits your needs!
![Alt text](https://github.com/melanieshimano/picademy-ddr/blob/master/tutorial_photos/monitor_setup.jpg)

6.	Plug in the mouse, keyboard, HDMI/monitor, and power supply to the RPi to power turn on the RPi

7.	Install the packages listed in the __Prerequisites__ section through the RPi terminal

8.	Download the code file from the Github page, unzip the file, and save the DDR_CAMERA.py and auth.py files to the same file

9.	Follow the instructions [here](https://projects.raspberrypi.org/en/projects/getting-started-with-the-twitter-api/2) to set up a Twitter account and get your access keys/tokens to make the Twitter bot portion of the RPi DDR game. Edit the auth.py file with your consumer key, consumer secret, access token, and access token secret information

10.	Make sure that your camera is set up at a good angle by following the [Getting Started with picamera](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera) instructions if you haven’t previously worked with the RPi camera

11.	Run the DDR_Camera file, do the dance, see it post on your [Twitter account](https://twitter.com/Picademy_DDR), and enjoy!
![Alt text](https://github.com/melanieshimano/picademy-ddr/blob/master/tutorial_photos/dog_gif.gif)
