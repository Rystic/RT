from readers.wasd_reader import WASDReader
from writers.simulated_writer import SimulatedWriter
import robot_runner

robot_runner.execute(WASDReader("rt"), SimulatedWriter())

# generate a random name
