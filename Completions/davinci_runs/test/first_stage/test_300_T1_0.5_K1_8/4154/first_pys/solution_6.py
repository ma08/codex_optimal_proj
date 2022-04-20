

N, M = map(int, input().split())

left = [0] * (N+1)
right = [0] * (N+1)

for _ in range(M):
    L, R = map(int, input().split())
    left[L] += 1
    right[R] += 1

for i in range(1, N+1):
    left[i] += left[i-1]

for i in range(N-1, -1, -1):
    right[i] += right[i+1]

ans = 0
for i in range(1, N+1):
    if left[i] == right[i]:
        ans += 1

print(ans)