#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 16:35:47 2020


@author: mauricio
"""
import sys

def main():
    message = input()
    message = message.split(" ")

    for i in range(0,len(message)):
        message[i] = int(message[i])

    message.sort()

    #print(message)

    count = 1

    for i in range(0,len(message)):
        if i != len(message) - 1:
            if message[i] == message[i+1]:
                count += 1
            else:
                print(message[i], end = " ")
                count = 1
        else:
            print(message[i], end = " ")

if __name__ == "__main__":
    main()
