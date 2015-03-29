# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 23:07:17 2015
le main encryption script
@author: qingwei
"""

import conversion
import cryptography
import subprocess

def str_from_file(path):
    with open(path, 'r') as f:
        data = f.read()
    return data

def str_to_file(path, s):
    with open(path, 'w') as f:
        f.write(s)

def ls():
    return subprocess.check_output(["ls"], universal_newlines=True)

def main():
    inputtext = input("Please enter string to be encrypt : \n")
    key = input("\nPlease enter int as key : \n")
    key = int(key)
    inputtextbit = conversion.string_to_bin(inputtext)

    print("\nthis is the raw input string in binary form : ")
    print(inputtextbit.to01())
    
    encryptedbit = cryptography.encrypt(inputtextbit, key)

    print("\nthis is the encrypted string in binary : ")
    print(encryptedbit.to01())
    
    key = input("Please reenter the key to decrypt : \n")
    key = int(key)
    decryptedbit = cryptography.decrypt(encryptedbit, key)
    decryptedstr = conversion.bin_to_string(decryptedbit)
        
    print("\nthis is the decrypted message in binary : ")
    print(decryptedbit.to01())
    
    print("\nthis is the decrypted message :")
    print(decryptedstr)
    
if __name__ == '__main__':
    main()