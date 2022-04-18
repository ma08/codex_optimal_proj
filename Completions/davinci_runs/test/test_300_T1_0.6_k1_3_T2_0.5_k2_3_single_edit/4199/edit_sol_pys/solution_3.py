

N, M = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
sum = 0
right = 0
for left in range(N):
    while right < N and sum < M:
        sum += a[right]
        right += 1
    if sum == M:
        ans += 1
    sum -= a[left]

print(ans)
