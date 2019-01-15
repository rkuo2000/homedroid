### $pip3 install gTTS
### $pip3 install playsound
### $python gTTS.py hello en
from gtts import gTTS
from playsound import playsound
import sys

text = sys.argv[1]
sl = sys.argv[2]

tts = gTTS(text,lang=sl)
tts.save('gTTS.mp3')
playsound('gTTS.mp3')
