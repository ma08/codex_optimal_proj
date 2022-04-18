
n, k = map(int, input().split())
a = list(map(int, input().split()))

l = 1
r = 10**9

while l <= r:
    m = (l+r)//2

    if sum(1 for x in a if x <= m) >= k:
        r = m-1
    else:
        l = m+1

print(l if sum(1 for x in a if x <= l) == k else -1)
