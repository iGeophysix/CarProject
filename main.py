import serial
import os

from time import sleep
import serial

def get_serial_port():
    return "/dev/"+os.popen("dmesg | egrep ttyACM | cut -f3 -d: | tail -n1").read().strip()


ser = serial.Serial(get_serial_port(), 115200) # Establish the connection on a specific port

while True:
     bufferString =  ser.readline() # Read the newest output from the Arduino
     print bufferString
     if "ARDUINO_CAN_BUS" in bufferString:
         ser.write("PC_CAN_BUS")

     sleep(.1) # Delay for one tenth of a second