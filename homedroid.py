#-*- coding: utf-8 -*-
#
# HomeDroid - Dialogflow
#
import os
import requests
from sys import argv
from bottle import Bottle, request
from bs4 import BeautifulSoup
import apiai
import json
import serial
ser = serial.Serial('COM4', 9600)

FB_PAGE_TOKEN = "EAANFvjT1XoY"
FB_VERIFY_TOKEN = "verify me"
FB_GRAPH_API = 'https://graph.facebook.com/v2.10/me/messages?'
ApiAI_ACCESS_TOKEN = "9ef660"

# Setup Bottle Server
app = Bottle()

@app.get('/')
def hello():
    return "HomeDroid: Hello !"

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
    #print(data)
    if data['originalRequest']['data']:
        sender = data['originalRequest']['data']['sender']['id']
        message = data['originalRequest']['data']['message'] 
        text    = data['originalRequest']['data']['message']['text']
        print(sender, text)
        text = "robot moving"
        sendMessage(sender, text) # to Messenger
        print(text)
        ser.write(b'forward')     # to UART
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
