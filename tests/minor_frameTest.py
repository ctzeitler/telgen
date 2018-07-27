import unittest
import minor_frame 


class MinorFrameTest(unittest.TestCase):
    
    def test_parse(self):
        raw = bytearray([10, 1, 2])
        minor_frame_definition = minor_frame.Definition()

        minor_frame_definition.setlength("A", 8)
        minor_frame_definition.setlength("B", 8)
        minor_frame_definition.setbitpositions("A", 8)
        minor_frame_definition.setbitpositions("B", 16)
        testobject = minor_frame.MinorFrame(raw, minor_frame_definition)

        self.assertEquals(1, testobject.getvalue("A"))
        self.assertEquals(2, testobject.getvalue("B"))


    def test_parse_suppercommutation(self):
        raw = bytearray([10, 1, 2])
        minor_frame_definition = minor_frame.Definition()

        minor_frame_definition.setlength("A", 8)
        minor_frame_definition.setbitpositions("A", (8, 16))

        testobject = minor_frame.MinorFrame(raw, minor_frame_definition)

        self.assertListEqual([1, 2], testobject.getvalue("A"))

    def test_parse_identacrossbyteboundaries(self):
        raw = bytearray([10, 5, 160, 255])
        minor_frame_definition = minor_frame.Definition()

        minor_frame_definition.setlength("A", 6)
        minor_frame_definition.setbitpositions("A", 13)

        minor_frame_definition.setlength("B", 19)
        minor_frame_definition.setbitpositions("B", 13)

        testobject = minor_frame.MinorFrame(raw, minor_frame_definition)
        self.assertEquals(45, testobject.getvalue("A"))

        self.assertEquals(368895, testobject.getvalue("B"))


class DefinitionTest(unittest.TestCase):

    def test_setidentposition(self):
        testobject = minor_frame.Definition() 
        testobject.setbitpositions("DKS100", 104)
        self.assertEquals(104, testobject.getbitpositions("DKS100"))

        testobject.setbitpositions("ACK", (25, 156))
        self.assertTupleEqual((25,156), testobject.getbitpositions("ACK"))

    def test_setidentposition_negative(self):
        testobject = minor_frame.Definition()
        self.assertRaises(ValueError, testobject.setbitpositions, "CODY", -1)
        self.assertRaises(ValueError, testobject.setbitpositions, "CODY", (10, -5))
    
    def test_setidentposition_empty(self):
        testobject = minor_frame.Definition()
        self.assertRaises(ValueError, testobject.setbitpositions, "", 10)

    def test_getidentnames(self):
        testobject = minor_frame.Definition()
        testobject.setbitpositions("DKS100", 104)
        testobject.setbitpositions("ACK", (25, 156))
        self.assertCountEqual(["DKS100", "ACK"], testobject.getidentnames())

        testobject.setbitpositions("TEST1000", 50)
        self.assertCountEqual(["DKS100", "ACK", "TEST1000"], testobject.getidentnames())

    def test_setidentlength(self):
        testobject = minor_frame.Definition()
        testobject.setlength("DKS100", 4)
        testobject.setlength("TEST1000", 10)

        self.assertEqual(4, testobject.getlength("DKS100"))
        self.assertEqual(10, testobject.getlength("TEST1000"))

    def test_setidentlength_negative(self):
        testobject = minor_frame.Definition()
        self.assertRaises(ValueError, testobject.setlength, "CODY", -1)

    def test_setidentlength_emptyidentname(self):
        testobject = minor_frame.Definition()
        self.assertRaises(ValueError, testobject.setlength, "", 10)



if __name__ == "__main__":
    unittest.main()