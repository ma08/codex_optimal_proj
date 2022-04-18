#!/usr/bin/env python3

def shift(c, key):
    return chr((ord(c) + ord(key) - 2 * ord('A')) % 26 + ord('A'))

c = input()
k = input()
print("".join(shift(c[i], k[i % len(k)]) for i in range(len(c))))
