#!/usr/bin/python3

import pygame
import paho.mqtt.client as paho


photo_path = '/home/pi/Pictures'
font_path  = "/home/pi/escapee-greetor/Fonts/"
sound_path = "/home/pi/escapee-greetor/Sounds/"
music_path = "/home/pi/escapee-greetor/Music/"



#eef on_publish(client1,userdata,result):             #create function for callback
#    print("data published \n")
#    pass

#def on_connect(client1, userdata, flags, rc):
#    print("Connected with result code "+str(rc))
#    client1.subscribe("hottopic")

#def on_message(client1, userdata, msg):
#    msg.payload = msg.payload.decode("utf-8")
#    print(msg.payload)
#    if (msg.payload == 'me'):
#        print("msg received")
#        client1.disconnect()
#    else:
#        print("nothing to do")

def play_background_music():
    name = music_path + "mainbackground.mp3"
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()



def main():
	play_background_music()


main()