#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 19:59:06 2020

@author: jing
"""


binary = input("Enter a binary number: ")
binary = binary[::-1]

octal = []
for i in range(0, len(binary), 3):
    if i+3 > len(binary):
        octal.append(binary[i:])
    else:
        octal.append(binary[i:i+3])

octal = [str(int(x, 2)) for x in octal]
octal = "".join(octal[::-1])
print(octal)
