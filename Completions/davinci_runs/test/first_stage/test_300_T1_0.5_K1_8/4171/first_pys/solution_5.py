

#-----Solution-----

n, k = map(int, input().split())
a = list(map(int, input().split()))

def split(l):
    a = []
    b = []
    for i in l:
        if i % 2 == 0:
            a.append(i)
        else:
            b.append(i)
    return a, b

def get_min_ops(arr, k):
    if k == 1:
        return 0
    if len(arr) < k:
        return -1
    if len(arr) == k:
        return 1
    if len(arr) == k + 1:
        return 2
    if len(arr) > k:
        a, b = split(arr)
        if len(a) >= k:
            return get_min_ops(a, k)
        if len(a) == k - 1:
            return 1 + get_min_ops(b, k - len(a))
        if len(a) < k - 1:
            return 2 + get_min_ops(b, k - len(a))

print(get_min_ops(a, k))