import sys

N = int(sys.stdin.readline())
A = int(sys.stdin.readline())
print("Yes" if N % 500 <= A else "No")
