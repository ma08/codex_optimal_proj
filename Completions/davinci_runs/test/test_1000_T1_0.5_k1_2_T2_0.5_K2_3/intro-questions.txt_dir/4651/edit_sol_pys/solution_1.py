
from sys import stdin
from collections import deque

n = int(stdin.readline())

dq = deque()

for _ in range(n):
    line = stdin.readline().split()
    if line[0] == 'appendleft':
        dq.appendleft(line[1])
    else:
        dq.append(line[1])

print(*dq)
