#!/usr/bin/python


def pangram(string):
    check = "abcdefghijklmnopqrstuvwxyz"
    for char in check:
        if char not in string.lower():
            return False
    return True

s = input()
if pangram(s):
    print("pangram")
else:
    print("not pangram")
