import requests
import socket
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def push_init():
    

    url = 'https://www.pushsafer.com/api'
    post_fields = {
	"t" : 'Alarm',
	"m" : 'Alarm going off',
	"s" : 11,
	"v" : 3,
	"i" : 33,
	"c" : '#FF0000',
	"d" : 'a',
	"u" : 'https://www.pushsafer.com',
	"ut" : 'Open Pushsafer',
	"k" : '0S3YoMceEKWtCnneL9qM',
	}

    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()
    print(json)

def stop_init():
    

    url = 'https://www.pushsafer.com/api'
    post_fields = {
	"t" : 'Alarm',
	"m" : 'Alarm turned off',
	"s" : 11,
	"v" : 3,
	"i" : 33,
	"c" : '#FF0000',
	"d" : 'a',
	"u" : 'https://www.pushsafer.com',
	"ut" : 'Open Pushsafer',
	"k" : '0S3YoMceEKWtCnneL9qM',
	}

    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()
    print(json)
    


PUSH_APP = {
    'name': 'PUSH',
    'init': push_init,
    'stop': stop_init
}


if __name__ == '__main__':
    push_init()
    stop_init()
