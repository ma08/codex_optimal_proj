#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 16:36:34 2018
@author: mohituniyal
"""
import sys

def main():
    words = set()
    for line in sys.stdin:
        for word in line.split():
            if word.lower() in words:
                print('.', end=' ')
            else:
                print(word, end=' ')
                words.add(word.lower())
        print()

main()
