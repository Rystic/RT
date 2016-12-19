from readers.wasd_reader import WASDReader
from writers.simulated_writer import SimulatedWriter
import robot_runner
import random

names = ['Alpha', 'Curiosity 0', 'Wall-E', 'Voltron', 'Dalek', 'R.O.B.', 'Bioroid', 'Eli', 'Viktor']

nameIndex = random.randrange(0, len(names))

robot_runner.execute(WASDReader("rt"), SimulatedWriter())
