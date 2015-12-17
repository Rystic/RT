import time
import urllib
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

while 1:
    try:
        aResp = urllib.urlopen("http://robotapp-1041.appspot.com/rt");
        web_pg = aResp.read();
        instruction = web_pg[15:19]
        if (instruction != 'None'):
            hexInstruction = hex(int(instruction, 2))[2]
            print hexInstruction
            ser.write(hexInstruction)
        time.sleep(.1)
    except IOError:
        time.sleep(5)
