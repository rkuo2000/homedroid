import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.layers import Flatten, Dense, Dropout
import random
import json
import pickle
import sys
import os
import speech_recognition as sr
from gtts import gTTS
import requests
import urllib.request
import time

recognizer = sr.Recognizer()
microphone = sr.Microphone(sample_rate=16000)
sl = 'en'
tl = 'en'

with open("intents.json") as file:
    data = json.load(file)

with open("data.pickle", "rb") as f:
    words, labels, training, output = pickle.load(f)

tf.reset_default_graph()

# Load Model
model = keras.models.load_model('chatbot_dnn.h5')

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)

def playsound(filename):
    os.system('mpg321 '+filename) # RPi3
    #os.system('cmdmp3 '+filename) # PC
    #os.system('afplay '+filename) # MAC	
		
def speech2text():
    print("Speak:")
    audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language=sl)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio!")
        playsound('beep.mp3')		
        return None
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        playsound('beep.mp3')		
        return None
		
def text2speech(text,tl):
    tts=gTTS(text, lang=tl)
    filename='gSTT.mp3'
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

def chatbot(text):
    model = keras.models.load_model('chatbot_dnn.h5')
    results = model.predict(numpy.array([bag_of_words(text, words)]))
    print('confidence: '+str(numpy.max(results)*100))
    results_index = numpy.argmax(results)
    tag = labels[results_index]
    for tg in data["intents"]:
        if tg['tag'] == tag:
            responses = tg['responses']      
    return(random.choice(responses))
	
if __name__ == "__main__":
    print("Start talking with the bot (type quit to stop)!")
    playsound('ring.mp3')
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)	
        while True:
            inp = speech2text()
            if inp!=None:
                if inp=='exit':
                    break
                else:
                    text=chatbot(inp)
                    print(text)
                    text2speech(text,tl)
            else:
                time.sleep(1)
