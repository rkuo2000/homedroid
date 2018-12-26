### $pip3 install SpeechRecognition
### $pip3 install PyAudio
### $pip3 install fbchat
import speech_recognition as sr
import sys
from fbchat import Client
from fbchat.models import *


sample_rate = 48000
chunk_size = 512

sl = sys.argv[1]
r= sr.Recognizer()

fbclient = Client("your_email", "your_password") 
Homedroid_ID = '549565418854547'

with sr.Microphone(sample_rate=sample_rate, chunk_size=chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    while True:
        print("Speak:")
        audio = r.listen(source)
        print("Processing...")
        try:
            text = r.recognize_google(audio, language=sl)
            print("You said:", text)
            fbclient.send(Message(text=text), thread_id=Homedroid_ID, thread_type=ThreadType.USER)
        except sr.UnknownValueError:
            print("Could not understand audio!")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
