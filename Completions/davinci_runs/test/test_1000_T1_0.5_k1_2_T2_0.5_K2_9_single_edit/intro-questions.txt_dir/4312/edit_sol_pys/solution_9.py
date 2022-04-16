

import sys

A,B,C,D = map(int, sys.stdin.readline().split())

if A>C or (A==C and B>D):
    print("Yes")
else:
    print("No")
