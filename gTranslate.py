import speech_recognition as sr
from gtts import gTTS
import requests
import urllib.request
import sys
import os
import random
from fbchat import Client
from fbchat.models import *

fb_account = 'akuo1997@yahoo.com'
fb_passwd = 'ariana123'

#sl = 'en' # source language
#tl = 'fr' # target language
sl = sys.argv[1]
tl = sys.argv[2]

sample_rate = 48000
chunk_size = 512
r= sr.Recognizer()

greeting =[]
tone =['tone0.mp3','tone1.mp3','tone2.mp3','tone3.mp3','tone4.mp3']
vocal=['vocal0.mp3','vocal1.mp3','vocal2.mp3','vocal3.mp3','vocal4.mp3','vocal5.mp3','vocal6.mp3']
greeting.append(tone)
greeting.append(vocal)

def text2speech(text,tl):
    tts=gTTS(text, lang=tl)
    tts.save('gTTS.mp3')
    #os.system('madplay gTTS.mp3') # RPi3
    #os.system('vlc gTTS.mp3')     # PC
    os.system('afplay gTTS.mp3')   # MAC
    
def speech2text():
    with sr.Microphone(sample_rate=sample_rate, chunk_size=chunk_size) as source:
        print("Canceling ambient noise.....")
#        r.adjust_for_ambient_noise(source)
        print("Speak:")
        audio = r.listen(source)
        print("Processing.....")
        try:
            text = r.recognize_google(audio, language=sl)
            print("You said  :", text)		
            return text
        except sr.UnknownValueError:
            print("Could not understand audio!")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

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

def fb_send(text):
    client.send(Message(text=text),thread_id=client.uid, thread_type=ThreadType.USER)    

# Main Program
print("--------------------------------------")
client = Client(fb_account, fb_passwd)
t=1
while True:
    # Greeting
    i = random.randint(0,len(greeting[t])-1)
    #os.system('madplay mp3/'+greeting[t][i]) # RPi3
    #os.system('vlc mp3/'+greeting[t][i]))    # PC
    os.system('afplay mp3/'+greeting[t][i])   # MAC
    # Speech to Text
    text  = speech2text()
    fb_send(text)
    if text is not None:
        ttext = translate(text,sl,tl)
        fb_send(ttext)
        text2speech(ttext,tl)
    if text=="have a good day":
        break
    print("--------------------------------------")
client.logout()
