

import sys

k, a, b = map(int, sys.stdin.readline().split())

if a % k == 0:
    print("OK")
elif k > b:
    print("NG")
else:
    print("OK")