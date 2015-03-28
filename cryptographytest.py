# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:31:00 2015

@author: qingwei
"""
import unittest
import cryptography as crypt
from bitarray import bitarray

class TestCryptography(unittest.TestCase):
    
    def simple_add_op(self, bit, key):
        return bit & key    
    
    def test_XOR(self):
        a = bitarray("1001")
        b = bitarray("0110")
        c = bitarray(list(crypt.xor(a, b)))
        self.assertEqual(c, bitarray("1111"))

    def test_keygen(self):
        key1 = 10000
        key2 = 10000
        key3 = 11000

        klist1 = list(crypt.key_generator(key1, 10))
        klist2 = list(crypt.key_generator(key2, 10))
        klist3 = list(crypt.key_generator(key3, 10))

        self.assertEqual(klist1, klist2)
        self.assertNotEqual(klist1, klist3)

    def test_half(self):
        l1 = bitarray("10001000")
        l2 = bitarray("10001001")
        l3 = bitarray("100001000")

        l1right = crypt.rightHalf(l1)
        l1left = crypt.leftHalf(l1)

        l2right = crypt.rightHalf(l2)
        l2left = crypt.leftHalf(l2)

        self.assertEqual(l1right, l1left)
        self.assertEqual(l2right, bitarray("1001"))
        self.assertNotEqual(l2right, l2left)

        with self.assertRaises(ValueError):
            crypt.rightHalf(l3)
        with self.assertRaises(ValueError):
            crypt.leftHalf(l3)

    def test_swap(self):
        l1 = bitarray("100110011001")
        l2 = bitarray("011001100110")

        self.assertEqual(l2, crypt.swapLeftRight(l1))

    def test_shift(self):
        l1 = bitarray("10011001")
        l2 = crypt.shift_arr(l1, 3)

        self.assertEqual(l2, bitarray("00110011"))

    def test_reorder(self):
        li = [x for x in range(0, 64)]
        li_cp = list(li)
        key = list(crypt.key_generator(2099, 1))[0]
        li2 = crypt.reorder_list(li_cp, key)

        self.assertEqual(set(li), set(li2))
        self.assertNotEqual(li, li2)

    def test_sbox(self):
        text = bitarray("1001")
        key = bitarray("1100")
        sub = crypt.sboxlookup(text, key, 1)

        self.assertEqual(len(sub), 4)
        self.assertNotEqual(sub, text)

    def test_sub(self):
        with self.assertRaises(Exception):
            t1 = bitarray("100")
            k1 = bitarray("100")
            crypt.substitution1(t1, k1)

        with self.assertRaises(Exception):
            t1 = bitarray("1000")
            k1 = bitarray("100000")
            crypt.substitution1(t1, k1)

        s = ""
        k = ""
        for i in range(0, 64):
            s = s +"1"
            k = k + "0"

        t64 = crypt.substitution1(bitarray(s), bitarray(k))
        self.assertNotEqual(t64, bitarray(s))

    def test_perm(self):
        s = ""
        k = ""
        for i in range(0, 32):
            s = s +"10"
            k = k + "11"
        sa = bitarray(s)
        ka = bitarray(k)
        perm = crypt.permutation1(sa, ka)

        self.assertNotEqual(perm, sa)
        self.assertEqual(perm.count(), sa.count())
        pass

    def test_matrix_op(self):
        t = bitarray("010110001")
        k = bitarray("000111001")
        r = crypt.matrix_mul(t, k)
        
        self.assertEqual(r, bitarray("001110001"))

    def test_4op(self):
        s = ""
        k = ""
        for i in range(0, 32):
            s = s +"10"
            k = k + "11"

        sa = bitarray(s)
        ka = bitarray(k)

        optext = crypt.four_operation(sa, ka)
        self.assertEqual(len(sa), len(optext))
        self.assertNotEqual(sa, optext)

    def test_round(self):
        s = ""
        k = ""
        for i in range(0, 64):
            s = s +"10"
            k = k + "1"
        sa = bitarray(s)
        ka = bitarray(k)
        roundt = crypt.round_function(sa, crypt.four_operation, ka)

        self.assertEqual(len(roundt), len(sa))
        self.assertEqual(len(roundt)/2, len(ka))
        self.assertNotEqual(sa, roundt)

    def test_feistel(self):
        keys = [bitarray("0001"), bitarray("0010"), bitarray("0011")]
        
        bittext = bitarray("01100110")
        crypted1 = crypt.feistel_network_flow(bittext, self.simple_add_op, keys)
        crypted2 = crypt.feistel_network_flow(bittext, self.simple_add_op, keys)
        
        self.assertEqual(len(bittext), len(crypted1))
        self.assertNotEqual(bittext, crypted1)
        self.assertEqual(crypted1, crypted2)

    def test_encrypt_decrypt(self):
        key = 1000
        
        s = '01001000011000010110110001101111001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000'

        rawbit = bitarray(s)

        encrypted = crypt.encrypt(rawbit, key)      
        decrypted = crypt.decrypt(encrypted, key)
        
        self.assertEqual(decrypted, rawbit)
        self.assertNotEqual(encrypted, rawbit)
        pass

if __name__ == '__main__':
    unittest.main()
