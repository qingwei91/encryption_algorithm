# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 20:25:20 2015

@author: qingwei
"""

import conversion
import cryptography
import subprocess
import re

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

def encrypt():
    files = ls()
    selection = input("Please select the file you want to encrypt from the list below\n" +
        "".join(files))
        
    f = files[int(selection)]
    f = re.subn('\A[\d+]\.\s|\n\Z', "", f)[0]
    
    print("\nYou have chosen " + f + " as file to encrypt")
    key = input("\nPlease enter int as key : \n")
    s = str_from_file(f)
    s = conversion.string_to_bin(s)
    encrypted = cryptography.encrypt(s, key)
    
    encrypted_f = "encrypted_" + f
    str_to_file(encrypted_f, encrypted.to01())
    
    print("\n Your cipher text is in " + encrypted_f)
    
if __name__ == '__main__':
    encrypt()