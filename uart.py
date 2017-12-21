import serial
ser = serial.Serial('COM4', 9600)
while 1:
    line = ser.readline()
    print(line)
