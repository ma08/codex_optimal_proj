

import sys

k, a, b = map(int, sys.stdin.readline().split())

if a % k == 0 or b % k == 0 or (a // k) != (b // k):
    print("OK")
else:
    print("NG")