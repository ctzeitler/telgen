import time
import numpy
class Ident():

    def __init__(self, bitlength, value_generator=None):
        self.bitlength = bitlength 
      
        self.value_generator = value_generator
        if self.value_generator is None:
            self.value_generator = default_value_generator

def default_value_generator(sfid, timestamp):
    """
     @fn default_value_generator(sfid, timestamp)
     @param sfid the current sub-frame identifier
     @parm timestamp current time that the frame was "received"

     @brief Returns a value of sfid plus the timestamp.
     This is the implementation that will be used if no function
     is given to generate the given value.
     """
    result = sfid + timestamp
    return result 

def createMinorFrame(timestamp, sfid, idents):
    """
     @fn createMinorFrame(timestamp, sfid, *idents)

     @param timestamp current timestamp of this frame
     @param sfid current sub-frame identifier to associate with this frame
     @param *idents list of minor frames 
    """    
    minor_frame = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00')
    return minor_frame

def createMajorFrame(timestamp, time_diff, sfid, minor_frame_size, idents):
    """
     @fn createMajorFrame(timestamp, time_diff, sfid, *minor_frame_defintions)

     @param timestamp 

    """
def size_in_bytes(idents):
    """
     @fn size_in_bytes(*idents)

     @param *idents collection of idents

     @fn Gets the number of bytes need to represent all of the idents. 
     Since ident size is repsresented in bits, this may not fall on a flat
     number (a multiple of 8). Thus, this will call a ceiling function
     if the number of bits is not a multiple of 8.
    """
    bits = size_in_bits(idents)
    size_in_bytes =  numpy.ceil(bits / 8)
    return size_in_bytes 

def size_in_bits(idents):
    """
     @fn calculate_size(*idents)
     
     @param *idents collection of idents 

     @brief Gets the total bit length of all idents 
    """
    bit_counts = list()
    for ident in idents:
        bit_counts.append(ident.bitlength)
    total_bits = sum(bit_counts)
    return total_bits


#This is independent between all of the streams.
minor_frame_rate = 0

#This is shared between all of the streams.
major_frame_rate = 0