#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def encode(string):
    new_string = ""
    count = 1
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
        else:
            new_string += string[i] + str(count)
            count = 1
    new_string += string[-1] + str(count) # 不会超出范围
    return new_string

def decode(string):
    new_string = ""
    for i in range(0, len(string) - 1, 2):
        new_string += string[i] * int(string[i + 1])
    return new_string

def main():
    for line in sys.stdin:
        if line[0] == "E" or line[0] == "e":
            print(encode(line[2:].strip()))
        else:
            print(decode(line[2:].strip()))

if __name__ == '__main__':
    main()
