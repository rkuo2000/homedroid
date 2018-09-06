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

def read_yaw():
    ln = s.readline()
    return int(ln)

if __name__ == '__main__':
    setup()
    print('reading IMU yaw...')
    while 1:
        print('Yaw= '+str(read_yaw()))
