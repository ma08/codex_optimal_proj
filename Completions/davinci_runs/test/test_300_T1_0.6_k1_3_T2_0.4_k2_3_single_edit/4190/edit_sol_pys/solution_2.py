import sys


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

c = []
for i in range(n):
    c.append((a[i]+b[i])%n)

c2 = sorted(c)

for i in range(n):
    b[c.index(c2[i])] = i

print(" ".join(map(str, b)))
