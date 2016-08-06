from abstract_writer import AbstractWriter

class SimulatedWriter(AbstractWriter):
    
    def write(self, input):
        if self.isValidInstruction(input):
            print input
