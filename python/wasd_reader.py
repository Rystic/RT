import urllib

from abstract_reader import AbstractReader

class WASDReader(AbstractReader):
    
    def __init__(self, name):
        super(WASDReader,self).__init__(name)

    def readInstruction(self):
        connected = super(WASDReader,self).readInstruction()
        if connected:
            aResp = urllib.urlopen("http://robotapp-1041.appspot.com/instruction?name=" + self.name)
            web_pg = aResp.read();
            instruction = web_pg[15:19]
            return instruction
        return None
