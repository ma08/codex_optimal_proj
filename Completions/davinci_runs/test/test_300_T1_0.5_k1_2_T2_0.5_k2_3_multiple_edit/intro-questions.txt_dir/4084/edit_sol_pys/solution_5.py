N = int(input())
R = [int(input()) for i in range(N)]
R.sort()
ans = 0
for i in range(N):
    ans = max(ans, R[i] * (N - i))
print(ans)
