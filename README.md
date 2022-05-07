# EE250-Final-Project
Thomas Marks and Rohan Daniel

To compile code run the rpi_clock.py code on the pi and be sure to have the clock_api.py code in the same directory to ensure access to the clock api.
Next run the vm_control.p code in the vm terminal and be sure to include the push_api.py and coin_api.py in the same directory to ensure access to the push
api and bitcoin api.

Set up the rpi with the grove pi and esnure the button is connected to d3.

To set up push notifications you must download the pushsafer app on your iphone or android and register your device to your account. In the push_api.py code you must change the k field in the postfields list to your private key through the pushsafer website.

To set the alarm, input the time you want in 24 hour Los Angeles Time, press enter to acknowedge time in the vm, and then press the up arrow to send alarm time to the pi. It was implemented this way incase you typed the wrong time andc wanted to change it before sending it to the pi. The time is default set to off but if you press the down key the alarm is set to off on the pi.

External libraries used were the grove pi library.

Video Demo links:
1st part-https://www.youtube.com/watch?v=1uPTGAHxXHY
2nd part explaing MQTT-https://www.youtube.com/watch?v=FhV7G-dIzFo
