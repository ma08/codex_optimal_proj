
import sys
from collections import deque


N = int(sys.stdin.readline())
words = deque()

for _ in range(N):
    words.append(sys.stdin.readline().strip())

print('{:02}:{:02}'.format(h3, m3))
