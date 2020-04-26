### Usage : python linuxapi.py en
import speech_recognition as sr 
import cv2
import numpy as np
import os
import sys
import time
import psutil
import keyboard
import mouse

sl = sys.argv[1]
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def stop_app(app_exe):
    for process in psutil.process_iter():
        if process.name() == app_exe:
            os.system("kill -9 "+process.pid)
	
os.system("cd ~")
usr_dir   = os.system("pwd")
doc_dir   = usr_dir+"/Documents"
music_dir = doc_dir+"/My Music"
video_dir = doc_dir+"/My Videos"
pic_dir   = doc_dir+"/My Pictures"

with microphone as source:
	recognizer.adjust_for_ambient_noise(source)

	while True:
		print("Speak:")	
		audio = recognizer.listen(source)
		try:
			txt=" "
			text = recognizer.recognize_google(audio, language=sl)
			cmd = text.split(" ")
			print("You said:", text)
#			win32api.MessageBox(0, text, "Speak") 
			if text=='exit':
				print('Bye Bye, see you!')
				break
			if cmd[0]=='open':
				if cmd[1]=='Chrome' or cmd[1]=='browser':
					os.system(usr_dir+"/chrome")
			if cmd[0]=='search' or cmd[0]=='Google':
				if len(cmd)==1:
					txt=" "
				else:
					txt=" google.com/search?q="
					for i in range(1,len(cmd)):
						txt += cmd[i]+'+'
				os.system(usr_dir+"/chrome"+txt[:-1])
			if cmd[0]=='watch' or cmd[0]=='YouTube':
				if len(cmd)==1:
					txt=" youtube.com "
				else:
					txt=" youtube.com/search?q="
					for i in range(1,len(cmd)):
						txt += cmd[i]+'+'
				os.system(usr_dir+"/chrome"+txt[:-1])
			if cmd[0]=='scroll':
				if len(cmd)>1:
					if cmd[1]=='up':
						keyboard.send('page up')
					if cmd[1]=='down':
						keyboard.send('page down')					
			if cmd[0]=='move':
				if len(cmd)>1:
					if cmd[1]=='up':
						keyboard.send('arrow up')
					if cmd[1]=='down':
						keyboard.send('arrow down')
			if cmd[0]=='play' or cmd[0]=='click':	
				mouse.click()				
			if cmd[0]=='close' or cmd[0]=='quit':
				if cmd[1]=='Chrome':
					stop_app('chrome.exe')
			if cmd[0]=='input':
				txt = text.replace(cmd[0]+" ","")+"\n"
				keyboard.write(txt)
				input_len=len(txt)
			if cmd[0]=='cancel':
				if cmd[1]=='input':
					#for i in range(input_len): keyboard.send('\b') # back_space
					stop_app('chrome')
		except sr.UnknownValueError:
			#print("Could not understand audio!")
			print("please say that again")
		except sr.RequestError as e:
			#print("Could not request results; {0}".format(e))
			pritn("please try again")
		print("")
