

from sys import stdin
n, k, q = [int(x) for x in stdin.readline().split()]
points = [k] * n

for _ in range(q):
    a = int(stdin.readline())
    points[a-1] += 1
    points = [p-1 for p in points]
for p in points:
    if p > 0:
        print("Yes")
    else:
        print("No")
