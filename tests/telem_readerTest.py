import unittest
import telem_reader 
import tempfile

class TelemReaderTest(unittest.TestCase):

    def setUp(self):
        self.sync_bytes = bytearray(b'<\xfe\x6b\x28\x40')
        self.telemetry_file = tempfile.TemporaryFile() 

    def tearDown(self):
        self.telemetry_file.close()

    def test_findsyncbytes(self):
        self.telemetry_file.write(self.sync_bytes)
        testobject = telem_reader.TelemReader(self.telemetry_file)
        start = testobject.find_frame_start(self.sync_bytes)
        self.assertEquals(0, start)        
    
    def test_findsyncbytes_notatstart(self):
        garbage = bytearray(10)
        minor_frame = bytearray(b'{\xfe\x6b\x28\x40}')
        self.telemetry_file.write(garbage)
        self.telemetry_file.write(minor_frame)

        testobject = telem_reader.TelemReader(self.telemetry_file)
        start = testobject.find_frame_start(self.sync_bytes)
        self.assertEquals(11, start)


if __name__ == "__main__":
    unittest.main()