

n, m = map(int, input().split())
a = list(map(int, input().split()))

coffee = sorted(a, reverse=True)

def check(k):
    total = 0
    for i in range(k):
        total += coffee[i] - i
        if total < 0:
            return False
    return True

lo, hi = 1, len(coffee)
while lo < hi:
    mid = (lo + hi) // 2
    if check(mid):
        hi = mid
    else:
        lo = mid + 1

if check(lo):
    print(lo)
else:
    print(-1)