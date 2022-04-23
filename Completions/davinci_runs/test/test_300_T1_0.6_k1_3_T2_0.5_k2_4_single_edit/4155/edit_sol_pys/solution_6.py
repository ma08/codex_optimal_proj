N = int(input())
A = list(map(int, input().split()))


ans = 0
for i in range(N):
    for j in range(i, N):
        ans = max(ans, A[i] ^ A[j])

ans = 0
for i in range(N):
    ans += abs(h[i] - (i + 1))

print(ans)
