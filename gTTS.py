### $pip3 install gTTS
from gtts import gTTS
import os

tts = gTTS('bonjour',lang='fr')
tts.save('gTTS.mp3')

#os.system('madplay gTTS.mp3') # RPi3
os.system('cmdmp3 gTTS.mp3')     # PC
#os.system('afplay gTTS.mp3')   # MAC
