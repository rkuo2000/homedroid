from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
import logging

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)
ask = Ask(app, '/')

#logging.getLogger("flask_ask").setLevel(logging.DEBUG)
logging.getLogger("flask_ask").setLevel(logging.ERROR)

@ask.intent('GPIOControlIntent', mapping={'status':'status', 'pin':'pin'})

def gpio_control(status, pin):
	try:
		pinNum = int(pin)
	except Exception as e:
		return statement('Pin number not valid.')
	GPIO.setup(pinNum, GPIO.OUT)
	if status in ['on','high']: GPIO.output(pinNum, GPIO.HIGH)
	if status in ['off','low']: GPIO.output(pinNum, GPIO.LOW)
	return statement('Turning pin {} {}'.format(pin, status))

if __name__ == '__main__':
	port = 5000 # the custom port you use
	app.run(host='0.0.0.0', port=port)
