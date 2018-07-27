import pandas
import minor_frame
from bytearrayvalueparser import ByteArrayValueParser as parser

class MajorFrame():

    def __init__(self, definition):
        self.definition = definition
        self.values = pandas.DataFrame()
        
    def parseminorframe(self, raw):
        sfid_length = self.definition.getsfidlength()
        sfid_position = self.definition.getsfidposition()        

        sfid = parser.parsevalue(raw, sfid_position, sfid_length)
        minor_frame_definition = self.definition.getframedefinition(sfid)

        frame = minor_frame.MinorFrame(raw, minor_frame_definition)
        data_frame = pandas.DataFrame.from_dict(frame.getvalues()) 
        data_frame.index = [(sfid, 10000)]
        print(data_frame.to_string())
        self.values = pandas.concat([self.values, data_frame])

    def getcurrentvalues(self):
       return self.values.copy()


class Definition():

    def __init__(self):
        self.definitions = dict()
        self.sfidposition = 0
        self.sfidlength = 8

    def setframedefinition(self, sfid, definition):
        if sfid < 0:
            raise ValueError("Cannot map minor frame definition to negative value ", sfid)
        self.definitions[sfid] = definition

    def getframedefinition(self, sfid):
        return self.definitions[sfid]
    
    def setsfidposition(self, position):
        self.sfidposition = position

    def getsfidposition(self):
        return self.sfidposition

    def setsfidlength(self, length):
        self.sfidlength = length

    def getsfidlength(self):
        return self.sfidlength
