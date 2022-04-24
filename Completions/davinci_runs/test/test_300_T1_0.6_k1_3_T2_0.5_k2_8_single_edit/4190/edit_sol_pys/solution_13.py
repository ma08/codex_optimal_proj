import sys


sys.stdin = open("input.txt", "r")

c = []
for i in range(n):
    c.append((a[i]+b[i])%n)

c2 = sorted(c)

for i in range(n):
    b[c.index(c2[i])] = i

print(" ".join(map(str, b)))
