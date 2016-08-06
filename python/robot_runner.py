from readers.abstract_reader import AbstractReader
from writers.abstract_writer import AbstractWriter
import time

def execute(reader, writer):

    while 1:
        instruction = reader.readInstruction()
        writer.write(instruction)
        time.sleep(.25)
