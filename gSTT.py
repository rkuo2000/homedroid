import speech_recognition as sr
from gtts import gTTS
import requests
import urllib.request
import sys
import os

sl = 'en' # source language
tl = 'fr' # target language

r= sr.Recognizer()

def gTranslate(text,sl,tl):
    btext = text.encode('utf-8')
    btext = str(btext).replace(" ","%20").replace("\\x","%")
    text = str(btext)[2:-1]
    print('Translate>',text)
    url="https://translate.google.com/m?hl=%s&sl=%s&q=%s" % (tl, sl, text)
    C_agent = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.165063 Safari/537.36 AppEngine-Google."}
    flag = 'class="t0">'
    request = urllib.request.Request(url, headers=C_agent)
    page = str(urllib.request.urlopen(request).read().decode(sys.getfilesystemencoding()))
    result = page[page.find(flag) + len(flag):]
    result = result.split("<")[0]
    return result

with sr.Microphone() as source:
#    r.adjust_for_ambient_noise(source)
    print("Speak:")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)		
        ttext = gTranslate(text,sl,tl)
        tts=gTTS(ttext, lang='fr')
        tts.save('gTTS.mp3')
        os.system('vlc gTTS.mp3')
    except sr.UnknownValueError:
        print("Could not understand audio!")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))