# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 22:00:16 2015

@author: qingwei
"""

import conversion
import cryptography
import subprocess
import re
from bitarray import bitarray

def str_from_file(path):
    with open(path, 'r') as f:
        data = f.read()
    return data

def str_to_file(path, s):
    with open(path, 'w') as f:
        f.write(s)

def ls():
    s = subprocess.check_output(["ls"], universal_newlines=True)
    s = s.split('\n')
    s = [str(i) + ". " + s[i] + "\n" for i in range(0, len(s)-1)]
    
    return s

def decrypt():
    files = ls()
    selection = input("Please select the file you want to decrypt from the list below\n" +
        "".join(files))
        
    f = files[int(selection)]
    f = re.subn('\A[\d+]\.\s|\n\Z', "", f)[0]
    
    print("\nYou have chosen " + f + " as file to decrypt")
    key = input("\nPlease enter int as key : \n")
    s = str_from_file(f)
    s = bitarray(s)
    decrypted = cryptography.decrypt(s, key)
    
    decrypted_f = "decrypted_" + f
    str_to_file(decrypted_f, decrypted.tostring())
    
    print("\n Your cipher text is in " + decrypted_f)
    
if __name__ == '__main__':
    decrypt()