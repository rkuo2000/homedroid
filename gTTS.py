### $pip3 install gTTS
from gtts import gTTS
import os

tts = gTTS('bonjour',lang='fr')
tts.save('gTTS.mp3')
#
os.system('vlc gTTS.mp3')
