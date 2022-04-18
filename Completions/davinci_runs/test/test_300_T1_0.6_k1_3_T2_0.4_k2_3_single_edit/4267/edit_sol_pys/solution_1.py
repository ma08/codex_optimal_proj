
import sys

N = int(sys.stdin.readline())

for i in range(N):
    X = int(sys.stdin.readline())
    if X >= 30:
        print("Yes")
    else:
        print("No")
