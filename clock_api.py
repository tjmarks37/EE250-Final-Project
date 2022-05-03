import requests
import socket
import json



def clock_init():
    

    response = requests.get('https://www.timeapi.io/api/Time/current/zone?timeZone=America/Los_Angeles')

    if response.status_code == 200: # Status: OK
        data = response.json()

        # TODO: Extract the time from the data
        hour=data['hour']
        minute=data['minute']
        seconds=data['seconds']
        
        time={
        	'hour':hour,
        	'minute':minute,
        	'seconds':seconds
        	}
       
        
        
        print(time)
        return time

    else:
        print('error: got response code %d' % response.status_code)
        print(response.text)
        return None


CLOCK_APP = {
    'name': 'Time in Los Angeles',
    'init': clock_init
}


if __name__ == '__main__':
    clock_init()
