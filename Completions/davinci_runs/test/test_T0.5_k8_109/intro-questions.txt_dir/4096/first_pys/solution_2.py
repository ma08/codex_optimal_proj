

# get input
n, m = map(int, input().split())
a = list(map(int, input().split()))

# solve
ans = 1
curr = 0
for i in range(n):
    if a[i] > ans:
        ans = a[i]
    curr += max(0, a[i] - ans + 1)
    if curr >= m:
        print(ans)
        break
else:
    print(-1)