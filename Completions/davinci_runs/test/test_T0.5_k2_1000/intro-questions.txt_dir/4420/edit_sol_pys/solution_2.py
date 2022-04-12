import sys

lines = sys.stdin.readlines()

for line in lines:
    x, y, n = map(int, line.split())
    print(n - (n % x) + y, end=' ')
