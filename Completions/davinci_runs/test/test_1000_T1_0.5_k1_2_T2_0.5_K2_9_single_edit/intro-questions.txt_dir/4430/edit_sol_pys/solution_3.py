
n, m, k = map(int, input().split())
a = list(map(int, input().split()))


def pack(a, m, k):
    res = 0
    j = 0
    for i in range(m):
        if j >= len(a):
            break
        while j < len(a) and a[j] <= k and res < m:
            k -= a[j]
            j += 1
            res += 1
        k = m - res
    return res

l = 0
r = n
while l < r:
    mid = (l + r) // 2
    if pack(a[:mid], k, m) < mid:
        l = mid + 1
    else:
        r = mid
print(l)
