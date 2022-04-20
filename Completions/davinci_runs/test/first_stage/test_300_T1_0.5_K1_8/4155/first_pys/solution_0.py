

from collections import deque

N = int(input())
h = deque(map(int, input().split()))

count = 0

while h:
    if h[0] >= h[-1]:
        h.popleft()
    else:
        h.pop()
    count += 1

print(count)