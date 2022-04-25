N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

A.sort()

ans = 0
for i in range(K + 1):
    diff = A[i + N - K] - A[i]
    if diff > ans:
        ans = diff

print(ans)
