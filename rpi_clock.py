import string
import requests
import paho.mqtt.client as mqtt
import time
import sys

sys.path.append('../../Software/Python/')

import grovepi
from grovepi import *

import clock_api

BTTN=3
grovepi.pinMode(BTTN,"INPUT")

if sys.platform == 'uwp':
    import winrt_smbus as smbus
    bus = smbus.SMBus(1)
else:
    import smbus
    import RPi.GPIO as GPIO
    rev = GPIO.RPI_REVISION
    if rev == 2 or rev == 3:
        bus = smbus.SMBus(1)
    else:
        bus = smbus.SMBus(0)

alarm_time="off"
flag=0
fg=0
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    
    client.subscribe("tom_rohan/alarm")
    client.message_callback_add("tom_rohan/alarm", alarm)
    client.subscribe("tom_rohan/button")
    client.message_callback_add("tom_rohan/button",button)
    

def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))
    
def button(client, userdata, message):
     global flag
     if str(message.payload, "utf-8") == "1":
        client.publish("tom_rohan/alarm_status","Alarm turned off")
        flag=0
     print(str(message.payload, "utf-8"))
        
       
            
def print_time(client, userdata, message): 
    print("Current Time (HR:MIN): " + str(message.payload, "utf-8"))
    

def alarm(client, userdata, message):
    global alarm_time
    global fg
    
    alarm_stat_new=str(message.payload, "utf-8")
    if alarm_stat_new != alarm_time:
        alarm_time=str(message.payload, "utf-8")
        fg=1
    if fg==1:
        print("Alarm time: " + str(message.payload, "utf-8"))
        fg=0
    
    
    #if str(message.payload, "utf-8")==current_time:  
     #   print("Alarm going off")       
          
          
if __name__ == '__main__':
    
    
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=1883, keepalive=60)
    client.loop_start()

    while True:
        time_list=clock_api.CLOCK_APP['init']()
        current_time=str(time_list['hour'])+":"+str(time_list['minute'])
        
        
        client.publish("tom_rohan/button", grovepi.digitalRead(BTTN))
        client.publish("tom_rohan/time", current_time)
        
        #if alarm_time==current_time:  
           #print("Alarm going off")
           #client.publish("tom_rohan/alarm_status","Alarm going off")
           #flag=1
           #alarm_time='off'
           #client.publish("tom_rohan/alarm", "off")
        #elif flag==1:
           #print("Alarm going off")
           #client.publish("tom_rohan/alarm_status","Alarm going off")
        
        if grovepi.digitalRead(BTTN)=="1" :
           print("Alarm off!")
           client.publish("tom_rohan/alarm_status","Alarm turned off")
           alarm_time="off"
           client.publish("tom_rohan/alarm", "off")
           
           #client.publish("tom_rohan/button", grovepi.digitalRead(BTTN))
           flag=0
           
        elif flag==0:
           client.publish("tom_rohan/alarm_status","Alarm not set")
           #flag=0
       
        	
           	
           
        
               
        time.sleep(1)

       
