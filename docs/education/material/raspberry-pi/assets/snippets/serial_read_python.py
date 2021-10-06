#/usr/bin/python3

import serial

PORT = '/dev/cu.usbmodem1421' # Change this to your port name (OSx format)
# PORT = '/dev/ttyACM0' # In linux
BAUDRATE = 115200

ser = serial.Serial(PORT, BAUDRATE)

while True:
    # Read the data 
    value = ser.readline().replace("\r\n", "")

    # Print it
    print (value)