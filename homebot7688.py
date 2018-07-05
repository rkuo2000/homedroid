# To run on Linkit7688
from sys import argv
from bottle import Bottle, request
import mraa
import time

# set GPIO pins to drive wheels (DC motors)
p31 = mraa.Gpio(14)
p30 = mraa.Gpio(15)
p29 = mraa.Gpio(16)
p28 = mraa.Gpio(17)
p31.dir(mraa.DIR_OUT)
p30.dir(mraa.DIR_OUT)
p29.dir(mraa.DIR_OUT)
p28.dir(mraa.DIR_OUT)
p31.write(0)
p30.write(0)
p29.write(0)
p28.write(0)

# Web API
app = Bottle()
@app.get('/hello')
def hello():
    return "Homebot7688> Hello !"

@app.get('/stop')
def stop():
    p31.write(0)
    p30.write(0)
    p29.write(0)
    p28.write(0)
    time.sleep(0.1)

@app.get('/forward')
def forward():
    p31.write(1)
    p30.write(0)
    p29.write(1)
    p28.write(0)
    time.sleep(0.1)

@app.get('/backward')
def backward():
    p31.write(0)
    p30.write(1)
    p29.write(0)
    p28.write(1)
    time.sleep(0.1)

@app.get('/turnright')
def forward():
    p31.write(0)
    p30.write(1)
    p29.write(1)
    p28.write(0)
    time.sleep(0.1)

@app.get('/turnleft')
def backward():
    p31.write(1)
    p30.write(0)
    p29.write(0)
    p28.write(1)
    time.sleep(0.1)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=argv[1])

