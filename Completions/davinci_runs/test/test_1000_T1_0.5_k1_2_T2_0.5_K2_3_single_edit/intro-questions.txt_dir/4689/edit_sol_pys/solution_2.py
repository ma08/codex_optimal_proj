

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(1, N):
    ans += max(0, A[i - 1] - A[i])

print(ans)
