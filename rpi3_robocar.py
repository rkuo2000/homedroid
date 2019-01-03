# Two-wheel Robo Car with Web API
from bottle import Bottle, request
import RPi.GPIO as GPIO
import time
import sys

app = Bottle()

# define control pins of TB6612FNG
PWMA = 17
AIN2 = 27
AIN1 = 22
BIN1 = 23
BIN2 = 24
PWMB = 25

# GPIO setup for motor control pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

# Robo functions
def robo_stop():
    GPIO.output(PWMB,GPIO.LOW)
    GPIO.output(BIN1,GPIO.LOW)
    GPIO.output(BIN2,GPIO.LOW)
    GPIO.output(PWMA,GPIO.LOW)
    GPIO.output(AIN1,GPIO.LOW)
    GPIO.output(AIN2,GPIO.LOW)

def robo_forward():
    GPIO.output(PWMB,GPIO.HIGH)
    GPIO.output(BIN1,GPIO.LOW)
    GPIO.output(BIN2,GPIO.HIGH)
    GPIO.output(PWMA,GPIO.HIGH)
    GPIO.output(AIN1,GPIO.LOW)
    GPIO.output(AIN2,GPIO.HIGH)

def robo_backward(): 
    GPIO.output(PWMB,GPIO.HIGH)
    GPIO.output(BIN1,GPIO.HIGH)
    GPIO.output(BIN2,GPIO.LOW)
    GPIO.output(PWMA,GPIO.HIGH)
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)

def robo_left():
    GPIO.output(PWMB,GPIO.HIGH)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)
    GPIO.output(PWMA,GPIO.HIGH)
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)

def robo_right():
    GPIO.output(PWMB,GPIO.HIGH)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)
    GPIO.output(PWMA,GPIO.HIGH)
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)

# Web API
@app.get('/hello')
def hello():
    return "RoboCar: Hello!!!"

@app.get('/stop')
def stop():
    robo_stop()
    return "RoboCar: Stop!"

@app.get('/forward')
def forward():
    robo_forward()
    time.sleep(0.1)
    robo_stop()
    return "RoboCar: move forward !"

@app.get('/backward')
def backward():
    robo_backward()
    time.sleep(0.1)
    robo_stop()
    return "RoboCar: move backward!"

@app.get('/left')
def left():
    robo_left()
    time.sleep(0.1)
    robo_stop()
    return "RoboCar: turn left!"

@app.get('/right')
def right():
    robo_right()
    time.sleep(0.1)
    robo_stop()
    return "RoboCar: turn right!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=sys.argv[1])
