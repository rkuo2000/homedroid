#
# Linkit7688 with Breakout board
#
# madplay "path_to_mp3_file"
# aplay -M "path_to_wav_file"
# arecord -f cd -t wav -M /Media/USB-A1/my_recording.wav

#import serial
import os
#import mraa
import time
import random

#comport  = '/dev/ttyS0'
#baudrate = 115200

#Meowing, Purring, Annoyed, Emphatic
cat_act = []
cat_act.append("Meowing")
cat_act.append("Purring")
cat_act.append("Annoyed")
cat_act.append("Emphatic")

while True:
    a = random.randint(0,2)
    i = random.randint(0,3)
    print(a, i)
    if a==3:
        mp3file = "Cat_"+cat_act[a]+".mp3"
    else:
        mp3file = "Cat_"+cat_act[a]+str(i)+".mp3"
    print(mp3file)
    os.system("madplay mp3/"+mp3file)
    time.sleep(2)
