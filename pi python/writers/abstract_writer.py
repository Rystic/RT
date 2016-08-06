class AbstractWriter(object):
    
    def write(self, input):
        print "No write method."

    def isValidInstruction(self, input):
        return input != 'None'
