
n, k = map(int, input().split())
a = list(map(int, input().split()))

l = 1
r = 10**9

while l < r:
    m = (l+r+1)//2

    if sum(1 for x in a if x <= m) >= k:
        r = m
    else:
        l = m

print(l)
