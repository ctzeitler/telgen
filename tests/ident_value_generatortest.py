import unittest
import ident_value_generator as gen

def _mult(sfid, timestamp):
    return sfid * timestamp

class IdentValueGeneratorTest(unittest.TestCase):

    def test_generatevalue(self):
        testobject = gen.IdentValueGenerator()

        name = "IDENT1000"
        testobject.set_generator(name, _mult)
        value = testobject.generate(name, 2, 2000) 

        self.assertEquals(4000, value)

    def test_generatevalue_nonegenerator(self):
        testobject = gen.IdentValueGenerator()

        name = "IDENT1000"
        testobject.set_generator(name, None)
        # When no function is specified, the value should be sin(sfid * timestamp)
        value = testobject.generate(name, 10, 100)

        expected = gen.default_generator(10, 100)
        self.assertAlmostEquals(expected, value)

    def test_generate_standard(self):
        testobject = gen.IdentValueGenerator()
        name = "STD45"
        testobject.set_generator(name)

        value = gen.default_generator(26, 1024)
        expected = gen.default_generator(26, 1024)
        self.assertAlmostEquals(expected, value)


if __name__ == "__main__":
    unittest.main()