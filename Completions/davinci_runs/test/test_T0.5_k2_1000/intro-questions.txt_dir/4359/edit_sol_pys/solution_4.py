
from sys import stdin

A = int(stdin.readline())
B = int(stdin.readline())
C = int(stdin.readline())
D = int(stdin.readline())
E = int(stdin.readline())

largest = 0
largest = max(largest, A)
largest = max(largest, B)
largest = max(largest, C)
largest = max(largest, D)
largest = max(largest, E)

print(largest)
