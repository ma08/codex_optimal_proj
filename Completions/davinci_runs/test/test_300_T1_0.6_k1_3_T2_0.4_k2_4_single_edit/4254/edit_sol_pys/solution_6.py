
import sys

A, B, C = map(int, sys.stdin.readline().split())

if A < B:
    if B < C:
        print("Yes")
    else:
        print("No")
elif A > B:
    if B > C:
        print("Yes")
    else:
        print("No")
else:
    print("No")
