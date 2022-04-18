
from sys import stdin

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    a = [int(x) for x in stdin.readline().strip().split()]
    b = [int(x) for x in stdin.readline().strip().split()]
    c = [0] * n
    for i in range(n):
        c[i] = a[i] + b[i]
    print(" ".join(str(x) for x in c))
