import time
import urllib
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

oldInstruction = '';

while 1:
    aResp = urllib.urlopen("http://robotapp-1041.appspot.com/");
    web_pg = aResp.read();
    instruction = web_pg[12]
    if instruction=='q':
        break
    if instruction!=oldInstruction:
        ser.write(instruction)
        oldInstruction=instruction
        print instruction
    time.sleep(.10)
