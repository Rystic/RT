from wasd_reader import WASDReader
from simulated_writer import SimulatedWriter
import time

wasdReader = WASDReader("rt")
simWriter = SimulatedWriter()

while 1:
    instruction = wasdReader.readInstruction()
    simWriter.write(instruction)
    time.sleep(.25)

# generate a random name
