import sys

n = int(input())
a = sorted([int(i) for i in sys.stdin.readline().split()])
Alice = 0
Bob = 0

for i in range(n):
    if i % 2 == 0:
        Alice += a[n - i - 1]
    else:
        Bob += a[n - i - 1]
print(Alice, Bob)
