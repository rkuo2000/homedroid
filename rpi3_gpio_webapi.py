# Two-wheel robo with Web API
from bottle import Bottle, request
import RPi.GPIO as GPIO
import time
import sys

app = Bottle()

# define motor control pins
MotorL_pin0 = 17
MotorL_pin1 = 27
MotorR_pin0 = 23
MotorR_pin1 = 24
Sensor_Front_pin = 4

# GPIO setup for motor control pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(MotorL_pin0, GPIO.OUT)
GPIO.setup(MotorL_pin1, GPIO.OUT)
GPIO.setup(MotorR_pin0, GPIO.OUT)
GPIO.setup(MotorR_pin1, GPIO.OUT)
GPIO.setup(Sensor_Front_pin, GPIO.IN)

# Robo functions
def robo_stop():
    GPIO.output(MotorL_pin0, GPIO.LOW)
    GPIO.output(MotorL_pin1, GPIO.LOW)
    GPIO.output(MotorR_pin0, GPIO.LOW)
    GPIO.output(MotorR_pin1, GPIO.LOW)

def robo_forward():
    GPIO.output(MotorL_pin0, GPIO.LOW)
    GPIO.output(MotorL_pin1, GPIO.HIGH)
    GPIO.output(MotorR_pin0, GPIO.LOW)
    GPIO.output(MotorR_pin1, GPIO.HIGH)

def robo_backward():
    GPIO.output(MotorL_pin0, GPIO.HIGH)
    GPIO.output(MotorL_pin1, GPIO.LOW)
    GPIO.output(MotorR_pin0, GPIO.HIGH)
    GPIO.output(MotorR_pin1, GPIO.LOW)

def robo_left():
    GPIO.output(MotorL_pin0, GPIO.HIGH)
    GPIO.output(MotorL_pin1, GPIO.LOW)
    GPIO.output(MotorR_pin0, GPIO.LOW)
    GPIO.output(MotorR_pin1, GPIO.HIGH)

def robo_right():
    GPIO.output(MotorL_pin0, GPIO.LOW)
    GPIO.output(MotorL_pin1, GPIO.HIGH)
    GPIO.output(MotorR_pin0, GPIO.HIGH)
    GPIO.output(MotorR_pin1, GPIO.LOW)

# Web API
@app.get('/hello')
def hello():
    return "HomeRobo: Hello!!!"

@app.get('/stop')
def stop():
    robo_stop()
    return "HomeRobo: Stop!"

@app.get('/forward')
def forward():
    robo_forward()
    time.sleep(1)
    robo_stop()
    return "HomeRobo: move forward !"

@app.get('/backward')
def backward():
    robo_backward()
    time.sleep(1)
    robo_stop()
    return "HomeRobo: move backward!"

@app.get('/left')
def left():
    robo_left()
    time.sleep(1)
    robo_stop()
    return "HomeRobo: turn left!"

@app.get('/right')
def right():
    robo_right()
    time.sleep(1)
    robo_stop()
    return "HomeRobo: turn right!"

#bumper_sensor  = GPIO.input(Sensor_Front_pin) 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=sys.argv[1])
