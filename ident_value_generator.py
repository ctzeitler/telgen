import numpy

def default_generator(sfid, timestamp):
    return numpy.sin(sfid * timestamp)

class IdentValueGenerator():

    def __init__(self):
        self.generators = dict()

    def set_generator(self, name, generator=default_generator):
        if (generator is None):
            generator = default_generator
        self.generators[name] = generator

    def generate(self, name, sfid, timestamp):
        generator = self.generators[name] 
        value = generator(sfid, timestamp)
        return value
