
import sys
import io

n,k,q = map(int, input().split())

arr = [k] * n
for i in range(q):
    a = int(input())
    arr[a-1] -= 1

for i in range(n):
    if arr[i] <= 0:
        print("No")
    else:
        print("Yes")
