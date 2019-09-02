### python gTranslator.py en fr
import speech_recognition as sr
from gtts import gTTS
import requests
import urllib.request
import sys
import os
import random

sl = sys.argv[1]
tl = sys.argv[2]

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def text2speech(text,tl):
    tts=gTTS(text, lang=tl)
    filename='gSTT.mp3'
    tts.save(filename)
    #os.system('mpg321 '+filename)  # RPi3
    os.system('cmdmp3 '+filename)  # PC
    #os.system('afplay '+filename)  # MAC
    os.remove(filename)
    
def speech2text():
    print("Speak:")        
    audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language=sl)
        os.system('aplay ring.wav')
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio!")
        os.system('aplay beep.wav')
        return None
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        os.system('aplay beep.wav')
        return None

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

if __name__ == "__main__":
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            text  = speech2text()
            if text is not None:
                ttext = translate(text,sl,tl)
                text2speech(ttext,tl)
            if text=="have a good day":
                break
