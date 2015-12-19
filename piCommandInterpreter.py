import time
import urllib
import sys
import requests
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

#establish connection


if len(sys.argv) < 2:
    print 'Error: No name provided.'
    sys.exit()
name = sys.argv[1]
print 'Name:', str(name)

r = requests.post("http://robotapp-1041.appspot.com/register", data={'name' : name})

while 1:
    try:
        aResp = urllib.urlopen("http://robotapp-1041.appspot.com/rt");
        web_pg = aResp.read();
        instruction = web_pg[15:19]
        if (instruction != 'None'):
            hexInstruction = hex(int(instruction, 2))[2]
            ser.write(hexInstruction)
        requests.post("http://robotapp-1041.appspot.com/heartbeat", data={'name' : name})
        time.sleep(.1)
    except IOError:
        time.sleep(5)
