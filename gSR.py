### $pip3 install SpeechRecognition
### $pip3 install PyAudio
import speech_recognition as sr
import sys

sl = sys.argv[1]
recognizer = sr.Recognizer()
microphone = sr.Microphone()

while True:
    print("Speak:")	
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)	
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language=sl)
            print("You said:", text)
        except sr.UnknownValueError:
            print("Could not understand audio!")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
    print("")
