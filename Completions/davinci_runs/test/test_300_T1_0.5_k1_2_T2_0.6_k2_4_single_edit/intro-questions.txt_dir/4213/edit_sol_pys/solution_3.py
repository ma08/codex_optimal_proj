

N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = A[-1] - A[0]
for i in range(1, N):
    ans = min(ans, A[i] - A[i-1])
print(ans)
