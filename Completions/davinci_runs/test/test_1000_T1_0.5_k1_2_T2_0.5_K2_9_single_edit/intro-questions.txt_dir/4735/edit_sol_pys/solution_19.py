
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:41:07 2020

@author: jacquelinedowling
"""

import os


#file_path = 'C:/Users/jacqu/Documents/GitHub/ECE-143-Project/test_file.txt'

def read_file(file_path):
    with open(file_path, 'r') as f:
        
        lines = f.readlines()
        lines = [x.strip() for x in lines]
        
        for line in lines:
            print(line)
        
        return lines


#read_file(file_path)
