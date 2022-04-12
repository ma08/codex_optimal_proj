import math

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

for i in range(n):
    for j in range(1, d+1):
        if j % (a[i] + 1) == 0:
            x -= 1

print(x)
