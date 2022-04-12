

n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

ans = 0
cnt = 0

for i in range(n):
    if cnt >= k or (cnt > 0 and a[i] - a[i-1] > k):
        cnt = 0
        ans += 1
    cnt += 1

if cnt > 0:
    ans += 1

print(ans)
