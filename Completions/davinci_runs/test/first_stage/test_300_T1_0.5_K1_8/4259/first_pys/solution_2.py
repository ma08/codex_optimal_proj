

import sys

K = int(sys.stdin.readline())
A, B = map(int, sys.stdin.readline().split())

for i in range(A, B + 1):
    if i % K == 0:
        print("OK")
        exit()

print("NG")