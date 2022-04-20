

# Solution

N = int(input())
A = [int(x) for x in input().split()]

A.sort()

res = 1
cur = A[0]

for i in range(1, N):
    if A[i] != cur:
        res += 1
    cur = A[i]

print(res)