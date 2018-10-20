# $pip3 install gTTS
from gtts import gTTS
tts = gTTS('bonjour',lang='fr')
tts.save('bonjour.mp3')
