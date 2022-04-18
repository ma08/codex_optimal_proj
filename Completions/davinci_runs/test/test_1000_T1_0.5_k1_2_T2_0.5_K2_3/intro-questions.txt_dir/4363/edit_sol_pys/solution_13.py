
N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0
for i in range(N):
    for j in range(i):
        ans += A[i] - A[j]
print(ans)
