import paho.mqtt.client as mqtt
import time
from pynput import keyboard
import sys
sys.path.append('../../Software/Python/')

import push_api
import coin_api
alarm_stat="Alarm not set"
alarm_time='off'
flag=1
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here
    client.subscribe("tom_rohan/alarm_status")
    client.message_callback_add("tom_rohan/alarm_status", alarm_status)
    client.subscribe("tom_rohan/button")
    client.message_callback_add("tom_rohan/button",button)
    #client.subscribe("tom_rohan/time")
    #client.message_callback_add("tom_rohan/time", print_time)
    
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))
    
def button(client, userdata, message):
    global alarm_time
    if str(message.payload, "utf-8") == "1":
        bitval=coin_api.COIN_APP['init']()
        push_api.PUSH_APP['coin'](bitval)
        alarm_time='off'
        client.publish("tom_rohan/alarm", "off")
       
            
def print_time(client, userdata, message): 
    print("Current Time (HR:MIN): " + str(message.payload, "utf-8"))
    
          
def on_press(key):
    try: 
        k = key.char # single-char keys
    except: 
        k = key.name # other keys
    
    if k =='up':
        client.publish("tom_rohan/alarm", alarm_time)
    elif k == 'down':
        client.publish("tom_rohan/alarm", "off")
        
def alarm_status(client, userdata, message):
    global alarm_stat
    global flag
    
    alarm_stat_new=str(message.payload, "utf-8")
    if alarm_stat_new != alarm_stat:
        alarm_stat=str(message.payload, "utf-8")
        flag=1
        
    if str(message.payload, "utf-8")=="Alarm not set" and flag==1:
        print("Alarm Status: " + str(message.payload, "utf-8"))
        flag=0
    if str(message.payload, "utf-8")=="Alarm going off" and flag==1:
        push_api.PUSH_APP['init']()
        print("Alarm Status: " + str(message.payload, "utf-8"))
        flag=0
    if str(message.payload, "utf-8")=="Alarm turned off" and flag==1:
        push_api.PUSH_APP['stop']()
        print("Alarm Status: " + str(message.payload, "utf-8"))
        client.publish("tom_rohan/alarm", "off")
        flag=0
        
if __name__ == '__main__':
    #setup the keyboard event listener
    lis = keyboard.Listener(on_press=on_press)
    lis.start() # start to listen on a separate thread
    
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=1883, keepalive=60)
    client.loop_start()
    

    while True:
        alarm_time = input("Enter alarm time in format Hour:Minute: \n")
        
        time.sleep(1)
       
