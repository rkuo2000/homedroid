import serial

comport  = '/dev/ttyS0'
baudrate = 115200

s = None

def setup():
    global s
    s =  serial.Serial(comport, baudrate)
    print('Serial: '+comport+' @'+str(baudrate)+' bps')
    print('Reading Serial...')

def loop():
    ln = s.readline()
    print(ln)

if __name__ == '__main__':
    setup()
    while True:
        loop()
