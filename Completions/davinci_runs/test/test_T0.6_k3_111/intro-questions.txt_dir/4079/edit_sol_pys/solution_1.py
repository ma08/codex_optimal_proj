#!/usr/bin/env python3

def is_diverse(string):
    for i in range(len(string) - 1):
        if ord(string[i]) + 1 != ord(string[i+1]) and ord(string[i]) - 1 != ord(string[i+1]):
            return False
    return True

count = int(input())
for i in range(count):
    string = input()
    if is_diverse(string):
        print('Yes')
    else:
        print('No')
