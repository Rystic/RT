from readers.wasd_reader import WASDReader
from writers.serial_writer import SerialWriter
import time
import robot_runner

if len(sys.argv) < 2:
    print 'Error: No name provided.'
    sys.exit()

robot_runner.execute(WASDReader(sys.argv[1]), SerialWriter())
