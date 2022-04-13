# file.py

import sys

n, c = map(int, sys.stdin.readline().split()) #n is the number of characters in the message and c is the number of distinct characters.

message = list(map(int, sys.stdin.readline().split())) #the characters in the message

freq = [0] * (c + 1)

for i in message:
    freq[i] += 1

for i in range(len(freq)):
    if freq[i] > 0:
        print(str(i) * freq[i], end=' ')
