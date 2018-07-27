import pandas
import numpy

class TelemReader():

    def __init__(self, telemetry_file):
        self.telemetry_file = telemetry_file

    def find_frame_start(self, sync_bytes):
        start = -1
        length = len(sync_bytes)
        data = self.telemetry_file.read(length)

        while (True):
            data = self.telemetry_file.read(length)
            print(data)
         



