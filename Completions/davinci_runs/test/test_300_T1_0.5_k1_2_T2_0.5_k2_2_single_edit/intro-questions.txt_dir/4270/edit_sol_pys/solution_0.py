
import sys

num = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

for i in range(1, num):
    arr[i] = (arr[i-1] + arr[i]) / 2

print(v[0])
