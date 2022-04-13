# coding: utf-8

import sys

s = sys.stdin.readline().rstrip()

for i in range(97, 123): # ord('a') = 97, ord('z') = 122
    if chr(i) not in s: # ord('a') = 97, ord('z') = 122
        print(chr(i)) # ord('a') = 97, ord('z') = 122
        exit() # ord('a') = 97, ord('z') = 122
print("None") # ord('a') = 97, ord('z') = 122
