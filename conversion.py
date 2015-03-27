# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:22:09 2015

@author: qingwei
"""
import binascii
from bitarray import bitarray

block_size = 128
size_per_char = 8
char_per_block = int(block_size/size_per_char)

def string_to_bin(s):
    """binary should be in bit array where one character map to 8 bit"""

    # padding whitespace to end of string, so that length % 16 is 0    
    remainder_size = len(s) % char_per_block
    
    for a in range(0, char_per_block - remainder_size):
        s = s + " "
    
    # convert each char into int
    bin_arr = binascii.a2b_qp(s)
    bit_arr = bitarray()

    # change each int into bit array, and extend previous result
    for i in bin_arr:
        b_str = '{0:08b}'.format(i)
        bit_arr.extend(bitarray(b_str))
        
    return bit_arr
    
def bin_to_string(bit_arr):
    """bit_arr is bit array"""

    n = len(bit_arr)    
    
    if n % 8 != 0:
        raise ValueError("corrupted input")
        
#    ascii_code = [int(bit_arr[i:i+8].tostring(), 2) for i in range(0, n, 8)]
#    char_list = [chr(code) for code in ascii_code]
    
    return bit_arr.tostring()