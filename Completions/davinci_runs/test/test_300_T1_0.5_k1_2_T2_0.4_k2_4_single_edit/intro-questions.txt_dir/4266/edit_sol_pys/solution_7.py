
import sys

k, x = list(map(int, sys.stdin.readline().split()))

print(x - k + 1, end=" ")

for i in range(1, k):
    print(x - k + 1 + i, end=" ") 
