from bisect import bisect

n, k = map(int, input().split())
a = list(map(int, input().split()))

l = [0]*n

for i, x in enumerate(a):
    l[i] = l[i-1] + x

    if sum(1 for x in a if x <= m) >= k:
        r = m-1
    else:
        l = m+1

if sum(1 for x in a if x <= l) == k:
    print(l)
else:
    print(-1)
