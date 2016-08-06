from abstract_writer import AbstractWriter
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

class SimulatedWriter(AbstractWriter):
    
    def write(self, input):
        if self.isValidInstruction(input):
            hexInstruction = hex(int(instruction, 2))[2]
            ser.write(hexInstruction)
