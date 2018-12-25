### $pip3 install gTTS
## $python3 gTTS.py en hello
from gtts import gTTS
import os
import sys

sl = sys.argv[1]
text = sys.argv[2]

tts = gTTS(text, lang=sl)
tts.save('gTTS.mp3')

#os.system('mpg321 gTTS.mp3') # PiZero
#os.system('madplay gTTS.mp3') # RPi3
os.system('cmdmp3 gTTS.mp3')     # PC
#os.system('afplay gTTS.mp3')   # MAC
