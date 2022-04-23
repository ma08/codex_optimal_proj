

# n = number of stores
# m = number of energy drinks we want to buy
# a = price of one energy drink at each store
# b = max number of energy drinks we can buy at each store
n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

# binary search
# if we can buy m energy drinks with money x, then we can also buy m energy drinks with money y where y > x (same logic applies to if we cannot buy)
# therefore, we can use binary search to find the minimum money we need to buy m energy drinks (the minimum value of x that satisfies the condition)
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
