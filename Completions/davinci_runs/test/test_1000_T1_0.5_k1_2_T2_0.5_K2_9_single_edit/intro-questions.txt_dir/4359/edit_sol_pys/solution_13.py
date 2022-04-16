

from sys import stdin

A = int(stdin.readline())
B = int(stdin.readline())
C = int(stdin.readline())
D = int(stdin.readline())
E = int(stdin.readline())

last_number = 0
last_number = max(last_number, A)
last_number = max(last_number, B)
last_number = max(last_number, C)
last_number = max(last_number, D)
last_number = max(last_number, E)

print(last_number)
