

from sys import stdin

A = int(stdin.readline())
B = int(stdin.readline())
C = int(stdin.readline())
D = int(stdin.readline())
E = int(stdin.readline())

last = 0
last = max(A, B, C, D, E, last)

print(last)
