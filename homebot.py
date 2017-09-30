#-*- coding: utf-8 -*-
#
# Homebot
#
# History:
# v0.1 create PersistentMenu
#
import os
import requests
from sys import argv
from bottle import Bottle, request
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import re
import paho.mqtt.publish as publish

FB_PAGE_TOKEN = "xxxxxxxxxxxxxxxxxxxx"
FB_VERIFY_TOKEN = "verify me"
FB_GRAPH_API = 'https://graph.facebook.com/v2.10/me/messages?'

HOST_ADDR = '123.195.50.57'
HOST_PORT = 1883

# global variables
FrontDoorState = 0
LightsState = 0
TVsetState = 0
StereoState = 0
XmasState = 0

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
                        sendMessage(sender,text)
                        sendQuickReplies_Home(sender)						
                    except KeyError:
                        print('>>>KeyError=message-text!')
#-------------------QuickReplies Payload----------------------------------------
                    try:
                        quick_reply= message['quick_reply']
                        payload=quick_reply['payload']
                        print(sender,payload)
                        if payload=='USER_DEFINED_PAYLOAD_LIVINGROOM':
                            sendQuickReplies_LivingRoom(sender)
                        elif payload=='USER_DEFINED_PAYLOAD_FAMILYROOM':
                            sendMessage(sender,'Under Construction!!!')
                        elif payload=='USER_DEFINED_PAYLOAD_KITCHEN':
                            sendMessage(sender,'Under Construction!!!')
                        elif payload=='USER_DEFINED_PAYLOAD_MASTERROOM':
                            sendMessage(sender,'Under Construction!!!')							
                        elif payload=='USER_DEFINED_PAYLOAD_BEDROOM':
                            sendMessage(sender,'Under Construction!!!')
#-------------------QuickReplies Payload for LivingRoom--------------------------
                        if payload=='USER_DEFINED_PAYLOAD_LIVINGROOM_DOOR':
                            payload='turn on Door light'
                            sendMQTT_pub('NTOUEE/AIOT/LIVINGROOM/DOOR', payload)
                        elif payload=='USER_DEFINED_PAYLOAD_LIVINGROOM_CEILING':
                            payload='turn on Ceiling lights'						
                            sendMQTT_pub('NTOUEE/AIOT/LIVINGROOM/CEILING', payload)
                        elif payload=='USER_DEFINED_PAYLOAD_LIVINGROOM_TVSET':
                            payload='turn on TV'						
                            sendMQTT_pub('NTOUEE/AIOT/LIVINGROOM/TVSET', payload)
                        elif payload=='USER_DEFINED_PAYLOAD_LIVINGROOM_STEREO':
                            payload='turn on Stereo'						
                            sendMQTT_pub('NTOUEE/AIOT/LIVINGROOM/STEREO', payload)
                        elif payload=='USER_DEFINED_PAYLOAD_LIVINGROOM_XMAS':
                            payload='turn on Christmas light'						
                            sendMQTT_pub('NTOUEE/AIOT/LIVINGROOM/XMAS', payload)							
                    except KeyError:
                        print('>>>KeyError=message-quick_reply!')
                except KeyError:
                    print('>>>KeyError=message!')
#-------------------Postback Payload---------------------------------------------					
                try:
                    postback= messages[0]['postback']
                    payload = messages[0]['postback']['payload']
                    print(sender,payload)
                    if payload=='GET_STARTED_PAYLOAD': 
                        sendMessage(sender, 'Hi, I am HomeBot.')
                    if payload=='USER_DEFINED_PAYLOAD_SMARTHOME':
                        sendQuickReplies_Home(sender)
                    if payload=='USER_DEFINED_PAYLOAD_ABOUT':
                        sendMessage(sender,'AI enable Smarter Home !')
                        sendMessage(sender,'HomeBot provide interactive UI of smart home.')
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

def sendMQTT_pub(topic, payload):
    publish.single(topic, payload, qos=1, hostname=HOST_ADDR, port=HOST_PORT)
	
def sendQuickReplies_Home(sender):
    data = {
        'recipient': {'id':sender},
        'message': {
            "text":"Select:",
            "quick_replies":[
            {
                "content_type":"text",
                "title":"LivingRoom",
                "payload":"USER_DEFINED_PAYLOAD_LIVINGROOM"
            },
            {
                "content_type":"text",
                "title":"FamilyRoom",
                "payload":"USER_DEFINED_PAYLOAD_FAMILYROOM"
            },
            {
                "content_type":"text",
                "title":"Kitchen",
                "payload":"USER_DEFINED_PAYLOAD_KITCHEN"
            },
            {
                "content_type":"text",
                "title":"MasterRoom",
                "payload":"USER_DEFINED_PAYLOAD_MASTERROOM"
            },
            {
                "content_type":"text",
                "title":"BedRoom",
                "payload":"USER_DEFINED_PAYLOAD_BEDROOM"
            }			
            ]
        }
    }
    qs = 'access_token=' + FB_PAGE_TOKEN
    resp = requests.post(FB_GRAPH_API + qs, json=data)
    return resp.content
	
def sendQuickReplies_LivingRoom(sender):
    data = {
        'recipient': {'id':sender},
        'message': {
            "text":"Select:",
            "quick_replies":[
            {
                "content_type":"text",
                "title":"Door",
                "payload":"USER_DEFINED_PAYLOAD_LIVINGROOM_DOOR"
            },
            {
                "content_type":"text",
                "title":"Ceiling",
                "payload":"USER_DEFINED_PAYLOAD_LIVINGROOM_CEILING"
            },			
            {
                "content_type":"text",
                "title":"TV",
                "payload":"USER_DEFINED_PAYLOAD_LIVINGROOM_TVSET"
            },
            {
                "content_type":"text",
                "title":"Stereo",
                "payload":"USER_DEFINED_PAYLOAD_LIVINGROOM_STEREO"
            },
            {
                "content_type":"text",
                "title":"Xmas",
                "payload":"USER_DEFINED_PAYLOAD_LIVINGROOM_XMAS"
            }			
            ]
        }
    }
    qs = 'access_token=' + FB_PAGE_TOKEN
    resp = requests.post(FB_GRAPH_API + qs, json=data)
    return resp.content
	
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=argv[1])
