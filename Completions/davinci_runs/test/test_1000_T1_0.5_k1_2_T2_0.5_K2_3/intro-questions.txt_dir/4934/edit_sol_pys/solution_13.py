
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
for i in range(n):
    print(arr[i], end=' ')
