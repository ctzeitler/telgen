import collections
from bytearrayvalueparser import ByteArrayValueParser as parser
import copy

class MinorFrame():
    
    def __init__(self, raw, definition):

        self.raw = raw
        self.definition = definition 
        self.values = dict()

        self.sfid = self._parsevalue(
            definition.getsfidlength(),
            definition.getsfidposition())

        for ident_name in definition.getidentnames():
            length = definition.getlength(ident_name)
            positions = definition.getbitpositions(ident_name)

            if isinstance(positions, collections.Iterable):
                self.values[ident_name] = list()
                positions = sorted(positions)
                for position in positions:
                    value = self._parsevalue(length, position)
                    self.values[ident_name].append(value)
            else:
                position = positions
                self.values[ident_name] = self._parsevalue(length, position)

    def getsfid(self):
        return self.sfid 

    def _parsevalue(self, length, position):
        value = parser.parsevalue(self.raw, position, length)
        return value
    
    def getvalue(self, identname):
        return self.values[identname] 
    
    def getvalues(self):

        values = dict()
        for key, value in dict(self.values).items():
            if not isinstance(value, collections.Iterable):
                value_as_list = [(key, value)]
                bit = self.definition.getbitpositions(key)
                values[bit] = value_as_list
        return values
    
class Definition():

    INVALID_SFID = -1

    def __init__(self):
        self.ident_positions = dict()
        self.ident_lengths = dict()
        self.sfidposition = 0
        self.sfidlength = 8

    def setlength(self, identname, length):
        if not identname:
            raise ValueError("Cannot use empty ident name") 
        if length < 0:
            raise ValueError("Cannot set length to negative value ", length)
 
        self.ident_lengths[identname] = length

    def getlength(self, identname):
        return self.ident_lengths[identname]

    def setbitpositions(self, identname, positions):
        if not identname:
            raise ValueError("Cannot set to the empty string")

        if isinstance(positions, collections.Iterable):
            if any(position < 0 for position in positions):
                raise ValueError('Can not set bit position to negative value ', positions)
        # If we have hit this branch, then only one integer has been given (e.g. not a tuple)
        # This is the nominal case (e.g. the other case, which imlies suppercommutation)
        # is unlikely to happen.
        else:
            if positions < 0:
                raise ValueError('Can not set bit position to negative value ', positions)
        
        self.ident_positions[identname] = positions

    def getbitpositions(self, identname):
        return self.ident_positions[identname] 

    def setsfidposition(self, position):
        self.sfidposition = position

    def getsfidposition(self):
        return self.sfidposition

    def setsfidlength(self, length):
        self.sfidlength = length 

    def getsfidlength(self):
        return self.sfidlength

    def getidentnames(self):
        return list(self.ident_positions.keys())        
    