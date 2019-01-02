# Two-wheel robo controlled by RPi3
import RPi.GPIO as GPIO
import time

# define motor control pins
motorL_pin0 = 17
motorL_pin1 = 27
motorR_pin0 = 23
motorR_pin1 = 24

# GPIO setup for motor control pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(motorL_pin0, GPIO.OUT)
GPIO.setup(motorL_pin1, GPIO.OUT)
GPIO.setup(motorR_pin0, GPIO.OUT)
GPIO.setup(motorR_pin1, GPIO.OUT)

# Robo functions
def robo_stop():
    GPIO.output(motorL_pin0, GPIO.LOW)
    GPIO.output(motorL_pin1, GPIO.LOW)
    GPIO.output(motorR_pin0, GPIO.LOW)
    GPIO.output(motorR_pin1, GPIO.LOW)

def robo_forward():
    GPIO.output(motorL_pin0, GPIO.LOW)
    GPIO.output(motorL_pin1, GPIO.HIGH)
    GPIO.output(motorR_pin0, GPIO.LOW)
    GPIO.output(motorR_pin1, GPIO.HIGH)

def robo_backward():
    GPIO.output(motorL_pin0, GPIO.HIGH)
    GPIO.output(motorL_pin1, GPIO.LOW)
    GPIO.output(motorR_pin0, GPIO.HIGH)
    GPIO.output(motorR_pin1, GPIO.LOW)

def robo_left():
    GPIO.output(motorL_pin0, GPIO.HIGH)
    GPIO.output(motorL_pin1, GPIO.LOW)
    GPIO.output(motorR_pin0, GPIO.LOW)
    GPIO.output(motorR_pin1, GPIO.HIGH)

def robo_right():
    GPIO.output(motorL_pin0, GPIO.LOW)
    GPIO.output(motorL_pin1, GPIO.HIGH)
    GPIO.output(motorR_pin0, GPIO.HIGH)
    GPIO.output(motorR_pin1, GPIO.LOW)

# robo test-run
robo_forward()
time.sleep(1)
robo_stop()
#
robo_backward()
time.sleep(1)
robo_stop()
#
robo_left()
time.sleep(1)
robo_stop()
#
robo_right()
time.sleep(1)
robo_stop()
