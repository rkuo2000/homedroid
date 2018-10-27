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
chunk_size = 1024
r= sr.Recognizer()

def text2speech(text,tl):
    tts=gTTS(text, lang=tl)
    tts.save('gTTS.mp3')
    #os.system('madplay gTTS.mp3')  # RPi3
    #os.system('afplay gTTS.mp3')   # MAC
    os.system('vlc gTTS.mp3')     # PC    
    
def speech2text():
    with sr.Microphone(sample_rate=sample_rate, chunk_size=chunk_size) as source:
        r.adjust_for_ambient_noise(source)
        print("Speak:")
        audio = r.listen(source)
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

# Main Program - Speech Translation
text  = speech2text()
ttext = translate(text,sl,tl)
text2speech(ttext,tl)
