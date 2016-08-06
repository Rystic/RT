import time
import urllib
import sys
import requests
#import serial

#ser = serial.Serial('/dev/ttyACM0', 9600)

if len(sys.argv) < 2:
    print 'Error: No name provided.'
    sys.exit()
name = sys.argv[1]
print 'Name:', str(name)

registered = False

while 1:
    try:
        # instruction reader
        if not registered:
            requests.post("http://robotapp-1041.appspot.com/register", data={'name' : name})
            registered = True
            print "registered " + name
        else:
            aResp = urllib.urlopen("http://robotapp-1041.appspot.com/instruction?name=" + name)
            web_pg = aResp.read();
            instruction = web_pg[15:19]
            print instruction

            # instruction writer
            if (instruction != 'None'):
                hexInstruction = hex(int(instruction, 2))[2]
                ser.write(hexInstruction)

            requests.post("http://robotapp-1041.appspot.com/heartbeat", data={'name' : name})
        time.sleep(.25)
    except IOError:
        time.sleep(10)
        registered = False
