

from sys import stdin

A = int(stdin.readline())
B = int(stdin.readline())
C = int(stdin.readline())
D = int(stdin.readline())
E = int(stdin.readline())

last = 0
last = max(last, A, B, C, D, E)

print(last)
