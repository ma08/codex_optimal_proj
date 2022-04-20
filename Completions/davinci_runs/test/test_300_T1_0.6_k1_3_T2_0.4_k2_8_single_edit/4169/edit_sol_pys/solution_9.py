

n, m, x = map(int, input().split())
a = list(map(int, input().split()))

# binary search
# if we can buy m energy drinks with money x, then we can also buy m energy drinks with money y where y > x
# if we cannot buy m energy drinks with money x, then we cannot buy m energy drinks with money y where y < x
# therefore, we can use binary search to find the minimum money we need to buy m energy drinks
ok = 10**9*10**5 + 1
ng = 0
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    # if we can buy m energy drinks with money mid, then ok = mid
    # otherwise, ng = mid
    total = 0
    for i in range(n):
        total += min(mid // a[i], b[i])
    if total >= m:
        ok = mid
    else:
        ng = mid

print(ok)
