# Two-wheel robo controlled by RPi3
import RPi.GPIO as GPIO
import time

# define motor control pins
MotorL_pin0 = 17
MotorL_pin1 = 27
MotorR_pin0 = 23
MotorR_pin1 = 24
Sensor_Front_pin = 4

# GPIO setup for motor control pins
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

# read robo-sensors
bumper_sensor  = GPIO.input(Sensor_Front_pin) 
print(bumper_sensor)

