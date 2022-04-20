import sys

t = int(input())
for test in range(t):
    n, k = map(int, input().split())
    if n < k:
        print("1")
    else:
        print("%d" % (n // k + n % k))
