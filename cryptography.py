# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 17:36:50 2015

custom encryption using feistel network as framework

@author: qingwei
"""

import math
import random
import binascii
from bitarray import bitarray

# data is bit array, which is array of boolean

block_size = 128
size_per_char = 8
char_per_block = int(block_size/size_per_char)

def rightHalf(arr):
    n = len(arr)    
    if n%2 == 1:
        raise ValueError("array length should be even")    
    return arr[:int(n/2)]

def leftHalf(arr):
    n = len(arr)    
    if n%2 == 1:
        raise ValueError("array length should be even")    
    return arr[int(n/2)-1:]

def swapLeftRight(arr):
    """swap the right halves and left halves of arr"""
    n = len(arr)    
    if n%2 == 1:
        raise ValueError("array length should be even")    
    left = leftHalf(arr)
    right = rightHalf(arr)
    return left.extend(right)

def round_function(inputText, operation, key):
    """
    round function of feistel network
    operation should accept half of text and key
    """
    newLeft = rightHalf(inputText)
    newRight = xor(operation(leftHalf(inputText), key), rightHalf(inputText))
    newLeft.extend(newRight)
    return newLeft
    pass

def xor(a, b):
    """a and b should be iterable of equal len"""
    for i,j in zip(a, b):
        if i!=j:
            yield 1
        else:
            yield 0
            
def key_generator(key, n):
    """return a generator of keys in """
    random.seed(key)
    for i in range(1, n):
        k = random.randrange(0, 127, 1)
        k = '{0:08b}'.format(k)
        yield bitarray(k)
        
def feistel_network_flow(bittext, operation, iteration, keys):
    """
    flow can be used for encryption and decryption by reversing order of keys
    bittext is bitarray, operation is function(bittext, operation)
    """
    intermediate = bittext  #initialize
    for k in keys:
        intermediate = round_function(intermediate, operation, k)
        
    return swapLeftRight(intermediate)
    
def substitution1(text, key):
    """
    text and key are 128 bit array
    4 bit as an entry of look up table
    find party of key xor text
    when the parity is even, sub only block with 2 or more 1
    else sub block with 2 or more 0
    """
    
    pass

def permutation():
    """
    
    """