

from sys import stdin

A = int(stdin.readline())
B = int(stdin.readline())
C = int(stdin.readline())
D = int(stdin.readline())
E = int(stdin.readline())

last = 0
last = max(last, A+B+C+D)
last = max(last, A+B+C+E)
last = max(last, A+B+D+E)
last = max(last, A+C+D+E)
last = max(last, B+C+D+E)

print(last)
