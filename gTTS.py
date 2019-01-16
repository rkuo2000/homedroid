### $pip3 install gTTS
### $pip3 install playsound
### $python gTTS.py hello en
from gtts import gTTS
import sys
import os

text = sys.argv[1]
sl = sys.argv[2]

tts = gTTS(text,lang=sl)
tts.save('gTTS.mp3')
#os.system('mpg321 gTTS.mp3') # RPi
os.system('cmdmp3 gTTS.mp3')  # PC
#os.system('afplay gTTS.mp3')  # MAC

os.remove('gTTS.mp3')
