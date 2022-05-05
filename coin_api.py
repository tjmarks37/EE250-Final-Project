import requests
import socket
import json



def coin_init():
    

    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    if response.status_code == 200: # Status: OK
        data = response.json()

        # TODO: Extract the time from the data
        bitval=data.get('bpi').get('USD').get('rate')
        out=json.dumps(data,indent=4)
        print(bitval)
       
        
        
        
        return bitval

    else:
        print('error: got response code %d' % response.status_code)
        print(response.text)
        return None


COIN_APP = {
    'name': 'Time in Los Angeles',
    'init': coin_init
}


if __name__ == '__main__':
    coin_init()
