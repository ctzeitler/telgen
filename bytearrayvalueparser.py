import math

class ByteArrayValueParser():
    
    @staticmethod
    def parsevalue(raw, position, length):
        """
        position number of bits into frame ident is found
        length how many bits to read at position
        """
        # Find byte to start bit manipulation at.

        starting_byte = math.floor(position / 8) 
        ending_byte = math.ceil((position + length) / 8)

        concat_value = 0
        
        for i in range(ending_byte - starting_byte):
            current_byte_index = starting_byte + i
            current_byte = raw[current_byte_index] 
            concat_value = concat_value << 8
            concat_value = concat_value | current_byte

        bits_offset_left = position - (starting_byte * 8)
        bits_offset_right = (ending_byte * 8) - length - position 

        mask = ((2**length - 1)) << (bits_offset_right)

        value = (concat_value & mask) >> bits_offset_right
        return value