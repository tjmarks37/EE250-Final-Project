import string
import requests
import paho.mqtt.client as mqtt
import time
import sys

sys.path.append('../../Software/Python/')

#import grovepi
#from grovepi import *

import clock_api

alarm_time="off"
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest hegit addre
    client.subscribe("tom_rohan/alarm")
    client.message_callback_add("tom_rohan/alarm", alarm)
    client.subscribe("tom_rohan/button")
    client.message_callback_add("tom_rohan/button",button)
    #client.subscribe("tom_rohan/time")
    #client.message_callback_add("tom_rohan/time", print_time)

def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))
    
def button(client, userdata, message):
    
    if str(message.payload, "utf-8") == "1":
        print("Alarm off!")
        print("custom_callback: " + message.topic + " " + "\"" + 
            str(message.payload, "utf-8") + "\"")
       

    elif str(message.payload, "utf-8") == "0":
        print("Alarm on!")
        print("custom_callback: " + message.topic + " " + "\"" + 
            str(message.payload, "utf-8") + "\"")
            
def print_time(client, userdata, message): 
    print("Current Time (HR:MIN): " + str(message.payload, "utf-8"))
    #print("custom_callback: " + message.topic + " " + "\"" + 
        #str(message.payload, "utf-8") + "\"")
    #print("custom_callback: message.payload is of type " + 
          #str(type(message.payload)))

def alarm(client, userdata, message):
    print("Alarm time: " + str(message.payload, "utf-8"))
    global alarm_time
    alarm_time=str(message.payload, "utf-8")
    
    
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
        
        client.publish("tom_rohan/time", current_time)
        if alarm_time==current_time:  
           print("Alarm going off")
           client.publish("tom_rohan/alarm_status","Alarm going off")
               
        time.sleep(1)

       
