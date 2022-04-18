
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

if n <= k:
    print(n * x)
elif n > k:
    print(k * x + (n - k) * y)
