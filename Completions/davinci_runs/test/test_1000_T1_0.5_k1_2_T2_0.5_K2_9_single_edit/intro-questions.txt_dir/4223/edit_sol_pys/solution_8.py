
N, M = input().split()
N = int(N)
M = int(M)
A = list(map(int, input().split()))
A.sort()
A.reverse()
ans = 0
for i in range(M):
    if A[i] < 0:
        break
    ans += A[i]
print(ans)
