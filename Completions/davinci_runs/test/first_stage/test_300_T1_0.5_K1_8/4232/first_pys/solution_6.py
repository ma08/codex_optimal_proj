

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

def func(x):
    return sum(1 for e in a if e <= x)

def binary_search(l, r):
    while l <= r:
        m = (l + r) // 2
        if func(m) == k:
            return m
        elif func(m) > k:
            r = m - 1
        else:
            l = m + 1
    return -1

print(binary_search(1, 10**9))