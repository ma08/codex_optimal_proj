
import sys
import math

N = int(input())
A = list(map(int, input().split()))

def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = list(set(table))
    return table

ans = []
for i in range(N):
    ans.append(len(divisor(A[i])))

print(max(ans))
