#!/usr/bin/env python3

name = input("Enter a string: ")

i = 1

while i < len(name):
    if name[i] == name[i - 1]:
        name = name[:i] + name[i + 1:]
        i -= 1
    else:
        i += 1

print(name)
