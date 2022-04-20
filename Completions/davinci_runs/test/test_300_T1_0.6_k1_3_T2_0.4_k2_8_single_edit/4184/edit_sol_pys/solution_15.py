

N, M = map(int, input().split())
A = [int(x) for x in input().split()]

A.sort()
A.reverse()

ans = 0
for i in range(M):
    if i % 2 == 0:
        ans += A[i]
    else:
        ans -= A[i]

print(ans)
