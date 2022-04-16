
def pack(a, k, m):
    res = 0
    j = 0
    for i in range(m):
        if j >= len(a):
            break
        while j < len(a) and a[j] <= k:
            k -= a[j]
            j += 1
            res += 1
        k = m
    return res
