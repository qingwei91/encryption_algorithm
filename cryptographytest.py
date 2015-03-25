# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:31:00 2015

@author: qingwei
"""
import unittest
import cryptography as crypt
from bitarray import bitarray

class TestCryptography(unittest.TestCase):
    def test_XOR(self):
        a = bitarray("1001")
        b = bitarray("0110")
        c = bitarray(list(crypt.xor(a, b)))
        self.assertEqual(c, bitarray("1111"))

    def test_keygen(self):
    
if __name__ == '__main__':
    unittest.main()
