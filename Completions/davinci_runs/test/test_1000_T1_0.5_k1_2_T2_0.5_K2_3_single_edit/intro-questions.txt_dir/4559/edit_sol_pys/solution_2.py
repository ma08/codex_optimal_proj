
N = int(input())
A = [int(i) for i in input().split()]

res = 1
for i in range(N):
    res *= A[i]
    if res > 10**18:
        res = -1
        break
print(res)
