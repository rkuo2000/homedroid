import speech_recognition as sr
from gtts import gTTS
import requests
import urllib.request
import sys
import os
import random

sl = sys.argv[1]

sample_rate = 48000
chunk_size = 256
r= sr.Recognizer()

count = 0

def text2speech(text,tl):
    global count
    tts=gTTS(text, lang=tl)
    filename='gSTT'+str(count)+'.mp3'
    tts.save(filename)
    #os.system('mpg321 '+filename)  # PiZero
    #os.system('madplay '+filename) # RPi3
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

# Main Program
with sr.Microphone(sample_rate=sample_rate, chunk_size=chunk_size) as source:
    print("Canceling ambient noise.....")
    r.adjust_for_ambient_noise(source)
    while True:
        text  = speech2text()
        if text is not None:
            text2speech(text,sl)
        print("--------------------------------------")
