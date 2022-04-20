

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

ans = 0
for i in range(m):
  if a[i] >= n:
    ans = -1
    break
  n -= a[i]

if ans != -1:
  ans = n

print(ans)