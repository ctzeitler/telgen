import unittest
import major_frame
import minor_frame
import pandas

class MajorFrameTest(unittest.TestCase):

    def test_parse(self):

        major_frame_definition = major_frame.Definition()

        first_minor_frame_definition = minor_frame.Definition()
        first_minor_frame_definition.setlength("A", 8)
        first_minor_frame_definition.setbitpositions("A", 8)
        first_minor_frame_definition.setlength("CATS", 8)
        first_minor_frame_definition.setbitpositions("CATS", 16)

        second_minor_frame_definition = minor_frame.Definition()
        second_minor_frame_definition.setlength("B", 8)
        second_minor_frame_definition.setbitpositions("B", 8)

        third_minor_frame_definition = minor_frame.Definition()
        third_minor_frame_definition.setlength("C", 8)
        third_minor_frame_definition.setbitpositions("C", 8)

        major_frame_definition = major_frame.Definition()
        major_frame_definition.setsfidlength(8)
        major_frame_definition.setsfidposition(0)
        major_frame_definition.setframedefinition(0, first_minor_frame_definition)
        major_frame_definition.setframedefinition(1, second_minor_frame_definition)
        major_frame_definition.setframedefinition(2, third_minor_frame_definition)

        testobject = major_frame.MajorFrame(major_frame_definition)

        first_minor_frame = bytearray([0, 10, 45])
        testobject.parseminorframe(first_minor_frame)

        second_minor_frame = bytearray([1, 20])
        testobject.parseminorframe(second_minor_frame)

        third_minor_frame = bytearray([2, 30])
        testobject.parseminorframe(third_minor_frame) 

        expected = pandas.DataFrame({'A': [10], 'B' : [20], 'C' : [30]})
        data_frame = testobject.getcurrentvalues()
        print(data_frame.to_string())
        self.assertEqual(expected, data_frame) 


class DefinitionTest(unittest.TestCase):

    def test_setminorframe(self):
        testobject = major_frame.Definition()

        minor_frame_definition = minor_frame.Definition()
        minor_frame_definition.setlength("A", 10)
        minor_frame_definition.setbitpositions("A", 5)

        testobject.setframedefinition(0, minor_frame_definition)
        self.assertEquals(minor_frame_definition, testobject.getframedefinition(0))

    def test_setminorframe_negativesfid(self):
        testobject = major_frame.Definition()

        minor_frame_definition = minor_frame.Definition()
        self.assertRaises(ValueError, testobject.setframedefinition, -1, minor_frame_definition)

if __name__ == "__main__":
    unittest.main()