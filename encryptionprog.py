# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 23:07:17 2015
le main encryption script
@author: qingwei
"""

import conversion
import cryptography

def main():
    inputtext = input("Please enter string to be encrypt\n")
    key = input("Please enter int as key\n")
    key = int(key)
    inputtextbit = conversion.string_to_bin(inputtext)
    
    encryptedbit = cryptography.encrypt(inputtextbit, key)
#    encryptedstr = conversion.bin_to_string(encryptedbit)
#
#    print("this is your encrypted message : " + encryptedstr)
#    
    key = input("Please reenter the key to decrypt\n")
    key = int(key)
    decryptedbit = cryptography.decrypt(encryptedbit, key)
    decryptedstr = conversion.bin_to_string(decryptedbit)
    
    print("this is the decrypted message: \n" + decryptedstr)
    
if __name__ == '__main__':
    main()