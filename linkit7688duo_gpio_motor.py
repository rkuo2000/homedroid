#
# Linkit7688Duo read MPU6050 and control motor by GPIOs
#
import serial
import mraa
import time

comport  = '/dev/ttyS0'
baudrate = 115200

# initialize Motor GPIO control pins
D14 = mraa.Gpio(17)
D15 = mraa.Gpio(16)
D16 = mraa.Gpio(15)
D17 = mraa.Gpio(0)
D14.dir(mraa.DIR_OUT)
D15.dir(mraa.DIR_OUT)
D16.dir(mraa.DIR_OUT)
D17.dir(mraa.DIR_OUT)
D14.write(0)
D15.write(0)
D16.write(0)
D17.write(0)

s = None

def setup():
    global s
    s =  serial.Serial(comport, baudrate)
    print('Serial: '+comport+' @'+str(baudrate)+' bps')

def motor_command(cmd,val):
    print("Command: "+cmd+", Duration= "+str(val)+" ms")
    if cmd=='F': motor_forward(val)
    if cmd=='B': motor_backward(val)
    if cmd=='L': motor_left(val)
    if cmd=='R': motor_right(val)
    if cmd=='S': motor_stop()

def motor_stop(val):
    D14.write(0)
    D15.write(0)
    D16.write(0)
    D17.write(0)
    time.sleep(val/1000.0)

def motor_forward(val):
    D14.write(1)
    D15.write(0)
    D16.write(1)
    D17.write(0)
    time.sleep(val/1000.0)
    D14.write(0)
    D15.write(0)
    D16.write(0)
    D17.write(0)
    time.sleep(0.5)
         
def motor_backward(val):
    D14.write(0)
    D15.write(1)
    D16.write(0)
    D17.write(1)
    time.sleep(val/1000.0)
    D14.write(0)
    D15.write(0)
    D16.write(0)
    D17.write(0)
    time.sleep(0.5)

def motor_right(val):
    D14.write(1)
    D15.write(0)
    D16.write(0)
    D17.write(1)
    time.sleep(val/1000.0)
    D14.write(0)
    D15.write(0)
    D16.write(0)
    D17.write(0)
    time.sleep(0.5)
         
def motor_left(val):
    D14.write(0)
    D15.write(1)
    D16.write(1)
    D17.write(0)
    time.sleep(val/1000.0)
    D14.write(0)
    D15.write(0)
    D16.write(0)
    D17.write(0)
    time.sleep(0.5)

def delayms(val):
    time.sleep(val/1000.0)

if __name__ == '__main__':
    setup()
    print('Motor Test running...')
    motor_command('F',100.0)
    motor_command('B',100.0)
    motor_command('L',100.0)
    motor_command('R',100.0)
    motor_stop(1000.0)
