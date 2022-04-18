

from sys import stdin
from collections import deque

n = int(stdin.readline())

d = deque()

for _ in range(n):
    line = stdin.readline().split()
    if line[0] == 'append':
        d.append(line[1])
    elif line[0] == 'appendleft':
        d.appendleft(line[1])
    elif line[0] == 'pop':
        d.pop()
    else:
        d.popleft()

print(*d, sep=' ')
