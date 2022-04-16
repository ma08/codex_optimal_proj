#!/usr/bin/env python3

"""
CS373: Quiz #18 (5 pts)
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following program?
    (4 pts)

a bb ccc dddd eeeee
"""

def f (n) :
    if (n == 0) :
        return ""
    return f(n - 1) + " " + chr(ord("a") + n - 1) * n

print(f(5))


n, m = map(int, input().split())
key = input()
cipher = input()

plain = ""

# first n letters of plaintext are the same as the key
plain += key

# next m-n letters of plaintext are the ciphertext minus the corresponding letter of the key
for i in range(m-n):
    plain += chr((ord(cipher[i]) - ord(key[i]) + 26) % 26 + ord('a'))


print(plain)
