### $sudo apt install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
### $pip3 install PyAudio
### $pip3 install SpeechRecognition
import speech_recognition as sr
import sys

sample_rate = 48000
chunk_size = 512

sl = sys.argv[1]
r= sr.Recognizer()

with sr.Microphone(sample_rate=sample_rate, chunk_size=chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    print("Speak:")
    audio = r.listen(source)
    print("Processing...")
    try:
        text = r.recognize_google(audio, language=sl)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Could not understand audio!")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
