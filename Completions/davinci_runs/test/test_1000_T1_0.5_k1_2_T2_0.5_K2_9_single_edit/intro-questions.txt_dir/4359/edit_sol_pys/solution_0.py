
from sys import stdin

A = int(stdin.readline())
B = int(stdin.readline())
C = int(stdin.readline())
D = int(stdin.readline())
E = int(stdin.readline())
last = 0
last = max(last, A)
last = max(last, B)
last = max(last, C)
last = max(last, D)
last = max(last, E)
print(last)
