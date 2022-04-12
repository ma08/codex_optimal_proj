#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 21:42:42 2020

@author: suryakantkumar
"""

'''
Problem : Simon says is a game where "Simon" outputs a sequence of 10 characters (R, G, B, Y) and the user must repeat the sequence. 
Create a program that plays this game, except that the computer comes up with its own sequences and the user must input the answer.
'''


import random

n = int(input('Enter number of test cases : '))

for i in range(1, n+1):
    print('\nTest Case : ', i)
    print('Simon says : ', end = '')
    for j in range(10):
        print(random.choice(['R', 'G', 'B', 'Y']), end = '')
    print()
    print('You say : ', end = '')
    for j in range(10):
        print(random.choice(['R', 'G', 'B', 'Y']), end = '')
    print()
    print('\n')
