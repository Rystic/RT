import time
import requests

class AbstractReader(object):

    name = None
    registered = False
    
    def __init__(self, name):
        self.name = name
        print 'Name:', str(self.name)

    def readInstruction(self):
        try:
            self.checkRegistration()
            requests.post("http://robotapp-1041.appspot.com/heartbeat", data={'name' : self.name})
            
        except IOError:
            print "Error: registration failed or connetion interrupted for " + self.name
            self.registered = False
            time.sleep(10)
        return self.registered

    def checkRegistration(self):
        if not self.registered:
            requests.post("http://robotapp-1041.appspot.com/register", data={'name' : self.name})
            self.registered = True
            print "registered " + self.name
