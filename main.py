import serial
import os

from time import sleep
import serial



ser = serial.Serial("/dev/ttyACM1", 115200) # Establish the connection on a specific port



while True:
     bufferString =  ser.readline() # Read the newest output from the Arduino
     print bufferString
     if "ARDUINO_CAN_BUS" in bufferString:
         ser.write("PC_CAN_BUS")

     sleep(.1) # Delay for one tenth of a second