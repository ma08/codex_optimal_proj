import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
nums.sort()

if N == M:
    print("Yes")
else:
    print("No")
