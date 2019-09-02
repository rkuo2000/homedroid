### Usage: python gTranslate.py en fr
import random
import json
import sys
import os
from gtts import gTTS
import requests
import urllib.request

sl = sys.argv[1]
tl = sys.argv[2]

def text2speech(text,tl):
    tts=gTTS(text, lang=tl)
    filename='gSTT.mp3'
    tts.save(filename)
    #os.system('mpg321 '+filename)  # PiZero
    #os.system('madplay '+filename) # RPi3
    os.system('cmdmp3 '+filename)  # PC
    #os.system('afplay '+filename)  # MAC
    os.remove(filename)

def translate(text,sl,tl):
    btext = text.encode('utf-8')
    btext = str(btext).replace(" ","%20").replace("\\x","%")
    text = str(btext)[2:-1]
    url="https://translate.google.com/m?hl=%s&sl=%s&q=%s" % (tl, sl, text)
    C_agent = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.165063 Safari/537.36 AppEngine-Google."}
    flag = 'class="t0">'
    request = urllib.request.Request(url, headers=C_agent)
    page = str(urllib.request.urlopen(request).read().decode(sys.getfilesystemencoding()))
    result = page[page.find(flag) + len(flag):]
    result = result.split("<")[0]
    print("Translated:", result)
    return result
	
def chat():
    print("Start talking with the bot (type exit to stop)!")
    while True:
        text = input("Input: ")
        if text.lower() == "exit":
            break
        ttext = translate(text,sl,tl)
        text2speech(ttext,tl)

chat()
