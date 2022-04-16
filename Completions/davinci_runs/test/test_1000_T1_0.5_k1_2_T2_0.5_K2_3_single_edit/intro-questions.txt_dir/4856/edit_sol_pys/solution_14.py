#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 19:24:35 2019


@author: joscelynec
"""

def reverse_numbers(a,b):
    a = a[::-1]
    b = b[::-1]
    print(a if a > b else b)
