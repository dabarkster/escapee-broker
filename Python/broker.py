#!/usr/bin/python3

import os
import alsaaudio
import pygame
import paho.mqtt.client as paho

broker="192.168.56.220"
port=1883

photo_path = '/home/pi/Pictures'
music_path = "/home/pi/Music/"
font_path  = "/home/pi/escapee-greetor/Fonts/"
sound_path = "/home/pi/escapee-greetor/Sounds/"



pygame.init()

def set_volume():
	#m = alsaaudio.Mixer()
	#current_volume = m.getvolume() # Get the current Volume
	#m.setvolume(70) # Set the volume to 70%.
	pass 
	
def MQTT():
    client1= paho.Client("control1")                           #create client object
    client1.on_publish = on_publish                          #assign function to callback
    client1.connect(broker,port,60)                                 #establish connection
    client1.on_connect = on_connect
    client1.on_message = on_message
    ret= client1.publish("hottopic",": Welcome to ZoeIke Tech")                   #publish
    client1.loop_start()

def on_publish(client1,userdata,result):             #create function for callback
#    print("data published \n")
    pass

def on_connect(client1, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client1.subscribe("hottopic")

def on_message(client1, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")
    print(msg.payload)
    if (msg.payload == 'me'):
        print("msg received")
        client1.disconnect()
    else:
        print("nothing to do")

def play_background_music():
	print("Starting background music...looping forever")
	name = music_path + "mainbackground.mp3"
	pygame.mixer.music.load(name)
	pygame.mixer.music.play(-1)  #-1 = loop forever
	pygame.mixer.music.set_volume(1)



def main():
	MQTT()
	play_background_music()
	set_volume()
	while True:
		pass


main()