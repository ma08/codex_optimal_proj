

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

curr = 0
i = 0
while i < n:
    if curr >= m:
        break
    if a[i] <= curr + 1:
        curr += a[i]
        i += 1
    else:
        break

if curr >= m:
    print(i)
else:
    print(-1)