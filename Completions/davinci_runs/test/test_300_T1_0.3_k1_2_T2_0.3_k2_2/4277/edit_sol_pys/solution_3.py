
import sys

n, a, b = map(int, sys.stdin.readline().rstrip().split())  # n:個数, a:単価, b:上限

if n * a <= b:
    print(n * a)
else:
    print(b)
