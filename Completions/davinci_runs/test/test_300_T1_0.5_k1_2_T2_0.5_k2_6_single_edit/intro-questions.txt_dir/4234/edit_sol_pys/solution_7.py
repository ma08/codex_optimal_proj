

from collections import deque

n = int(input())
s = input()

d = deque()
for c in s:
    d.append(c)
    if len(d) > 1 and d[-1] == d[-2]:
        d.pop()
        d.pop()

print(n - len(d))
print(''.join(d))
