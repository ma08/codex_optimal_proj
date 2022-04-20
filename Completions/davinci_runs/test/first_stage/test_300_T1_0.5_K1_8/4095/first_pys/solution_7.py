

n, m = map(int, input().split())

a = list(map(int, input().split()))

from collections import defaultdict

def median(a):
    if len(a) % 2 == 1:
        return a[len(a) // 2]
    else:
        return a[len(a) // 2 - 1]

def preprocess(a):
    d = defaultdict(list)
    for i, val in enumerate(a):
        d[val].append(i)
    return d

d = preprocess(a)

def get_indexes(val, d):
    return d[val]

def get_median(a, l, r):
    return median(a[l:r])

def get_pairs(a, m, d):
    n = len(a)
    pairs = []
    for i, val in enumerate(a):
        if val != m:
            continue
        for j in get_indexes(m, d):
            l = min(i, j)
            r = max(i, j)
            if get_median(a, l, r) == m:
                pairs.append((l, r))
    return pairs


pairs = get_pairs(a, m, d)

print(len(pairs))