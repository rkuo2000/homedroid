#-*- coding: utf-8 -*-
#
# Homedroid
#
# Features:
#     using messenger to input commands
#     homedroid.py running on PC to send commands from UART to NodeMCU
import os
import requests
from sys import argv
from bottle import Bottle, request
from bs4 import BeautifulSoup
import json
import re
import serial
ser = serial.Serial('COM10', 9600)

FB_PAGE_TOKEN = "EAANFvjT1XoYBAHNOW"
FB_VERIFY_TOKEN = "verify me"
FB_GRAPH_API = 'https://graph.facebook.com/v2.10/me/messages?'

# Setup Bottle Server
app = Bottle()

@app.get('/')
def hello():
    return "Homebot: Hello !"

@app.get('/webhook')
def messenger_webhook():
	verify_token = request.query.get('hub.verify_token')
	if verify_token == FB_VERIFY_TOKEN:
		return request.query.get('hub.challenge')
	else:
		return 'Invalid Request or Verification Token'

@app.post('/webhook')
def messenger_post():
    """
    Handler for webhook (currently for postback and messages)
    """
    data = request.json
    if data['object'] == 'page':
        for entry in data['entry']:
            messages = entry['messaging']
            if messages[0]:
                sender  = messages[0]['sender']['id']
                try:
                    message = messages[0]['message']
#-------------------Message Text-----------------------------------------------
                    try:
                        text  = message['text']
                        print(sender,text)
                        if text=='Stop':
                            ser.write(b'stop\n')
                        if text=='Forward':
                            ser.write(b'forward\n')
                        if text=='Backward':
                            ser.write(b'backward\n')
                        if text=='TurnRight':
                            ser.write(b'turnRight\n')
                        if text=='TurnLeft':
                            ser.write(b'turnLeft\n')							
                    except KeyError:
                        print('>>>KeyError=message-text!')							
                    except KeyError:
                        print('>>>KeyError=message-quick_reply!')
                except KeyError:
                    print('>>>KeyError=message!')
                except KeyError:
                    print('>>>KeyError=postback!')
    else:
        return 'Received Different Event'

def sendMessage(sender, text):
	"""
	Function for sending message
	"""
	data = {
		'recipient':{'id': sender},
		'message'  :{'text': text}
	}
	qs = 'access_token=' + FB_PAGE_TOKEN
	resp = requests.post(FB_GRAPH_API + qs, json=data)
	return resp.content	
	
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=argv[1])
