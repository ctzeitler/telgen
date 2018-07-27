import unittest
import telem_generator as gen

class MinorFrameGenerator(unittest.TestCase):

    def test_sizeinbits(self):
        ident_one = gen.Ident(16)
        ident_two = gen.Ident(32) 
    
        bit_size = gen.size_in_bits([ident_one, ident_two])
        self.assertTrue(48, bit_size)

    def test_sizeinbytes(self):
        ident_one = gen.Ident(16)
        ident_two = gen.Ident(32)

        byte_size = gen.size_in_bytes([ident_one, ident_two])
        self.assertTrue(48/8, byte_size)

    def test_createminorframe(self):
        ident_one = gen.Ident(8, MinorFrameGenerator._mult)
        minor_frame = gen.createMinorFrame(1000, 20, [ident_one])
                

    def _mult(sfid, timestamp):
        result = sfid * timestamp
        return result

if __name__ == "__main__":
    unittest.main()