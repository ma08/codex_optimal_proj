
import sys

n = int(sys.stdin.readline())

a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))

a.sort()

b = []

for i in range(n):
    b.append(a.pop())
    if a and a[-1]*2 == b[-1]:
        b.append(a.pop())

print(' '.join(map(str, b)))
