from readers.wasd_reader import WASDReader
from writers.serial_writer import SerialWriter
import time

if len(sys.argv) < 2:
    print 'Error: No name provided.'
    sys.exit()

wasdReader = WASDReader(sys.argv[1])
serialWriter = SerialWriter()

while 1:
    instruction = wasdReader.readInstruction()
    serialWriter.write(instruction)
    time.sleep(.25)
