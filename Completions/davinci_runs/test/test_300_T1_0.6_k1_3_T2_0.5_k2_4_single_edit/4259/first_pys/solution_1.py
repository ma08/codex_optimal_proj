

import sys

K = int(sys.stdin.readline().rstrip())
A, B = map(int, sys.stdin.readline().rstrip().split())

if A % K == 0:
    print("OK")
elif (A // K + 1) * K <= B:
    print("OK")
else:
    print("NG")