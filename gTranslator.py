import speech_recognition as sr
from gtts import gTTS
import requests
import urllib.request
import sys
import os
import random

#sl = 'en' # source language
#tl = 'fr' # target language
sl = sys.argv[1]
tl = sys.argv[2]

sample_rate = 48000
chunk_size = 256
r= sr.Recognizer()

count = 0

def text2speech(text,tl):
    global count
    tts=gTTS(text, lang=tl)
    filename='gSTT'+str(count)+'.mp3'
    tts.save(filename)
    #os.system('mpg321 '+filename) # RPi3
    os.system('cmdmp3 '+filename)  # PC
    #os.system('afplay '+filename)  # MAC
    os.remove(filename)
    count += 1
    
def speech2text():
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

# Main Program
with sr.Microphone(sample_rate=sample_rate, chunk_size=chunk_size) as source:
    print("Canceling ambient noise.....")
    r.adjust_for_ambient_noise(source)
    while True:
        text  = speech2text()
        if text is not None:
            ttext = translate(text,sl,tl)
        text2speech(ttext,tl)
        if text=="have a good day":
            break
        print("--------------------------------------")