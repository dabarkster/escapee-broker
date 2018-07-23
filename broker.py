#!/usr/bin/python3

import os
import pyfirmata
import pygame
import random
import time
import paho.mqtt.client as paho
from time import sleep


photo_path = '/home/pi/Pictures/'
music_path = "/home/pi/Music/"
font_path  = "/home/pi/escapee-validator/Fonts/"
sound_path = "/home/pi/escapee-validator/Sounds/"
video_path = "/home/pi/escapee-validator/Videos/"

######################## PYFirmata Initialize ########################
board          = pyfirmata.Arduino('/dev/ttyACM0')
pin_keyswitch  = board.get_pin('d:x:i')
pin_bigbutt    = board.get_pin('d:x:i')
pin_plas1      = board.get_pin('d:x:o')
pin_plas2      = board.get_pin('d:x:o')
pin_analyzing  = board.get_pin('d:x:o')
pin_latch      = board.get_pin('d:x:o')
pin_latch_butt = board.get_pin('d:x:i')
pin_lightning  = board.get_pin('d:x:o')
pin_sending    = board.get_pin('d:x:o')
pin_uv         = board.get_pin('d:x:o')
#pin_fan always on
pin_fog        = board.get_pin('d:x:o')
pin_arm        = board.get_pin('d:x:o')

pin = board.get_pin('d:5:o')

######################## PY Initialize ########################

pygame.init()
pygame.font.init()
print("Validator!")

######################## MQTT Initialize ########################
topic           = "escapee/broker"
topicAll        = topic + "/#"
topicStatus     = topic + "/status"
topicCommand    = topic + "/command"
topicTimer      = topic + "/timer"
topic_validator = "escapee/validator/command"

broker="192.168.56.220"
port=1883

client.on_connect = on_connect
client.message_callback_add(topicCommand, on_message_command)
client.on_message = on_message
client.connect(broker_address, 1883, 60) #connect to broker
client.loop_start()
client.publish(topicStatus,"Starting")#publish
time.sleep(1) #slight delay to show starting status
client.publish(topicStatus,"Waiting")


######################## PY Functions ########################
def play_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()  #-1 = loop forever
    #pygame.mixer.music.set_volume(0.5)

def play_sound():
    pass

######################## Other Functions ########################

      

######################## MQTT Functions ########################

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topicAll)

def on_message(client, userdata, msg):
    pass

def on_message_command(client, userdata, msg):
   
    msg.payload = msg.payload.decode("utf-8")

    if "59" in msg.payload:
        client.publish(topicStatus,"59 Minutes")
        play_music("60.mp3")

    if "45" in msg.payload:
        client.publish(topicStatus,"45 Minutes")
        play_music("45.mp3")

    if "30" in msg.payload:
        client.publish(topicStatus,"30 Minutes")
        play_music("30.mp3")

    if "15" in msg.payload:
        client.publish(topicStatus,"15 Minutes")
        play_music("15.mp3")

    if "60" in msg.payload:
        client.publish(topicStatus,"60 Second")
        play_music("60.mp3")

    if "BOOM" in msg.payload:
        client.publish(topicStatus,"Lightning")
        client.publish(topic_validator,"lightning_on")
        time.sleep(300)
        client.publish(topic_validator,"lightning_off")

    if "background" in msg.payload:
        client.publish(topicStatus,"Background Music")
        play_music("background.mp3")


######################## Main ########################
def main():

    
    play_music("background.mp3")
    play_sound("alarm.wav")
    play_sound("securitybreach.wav")
    
    while True:
        pass

    quit()


if __name__ == "__main__":
    main()
