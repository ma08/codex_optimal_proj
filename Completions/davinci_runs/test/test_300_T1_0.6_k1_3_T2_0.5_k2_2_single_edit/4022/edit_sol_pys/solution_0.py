
def fun(v, n, k):
    v.sort()
    if n > 1:
        if v[n - 2] > k:
            return v[n - 2] - k
        else:
            return 0
    else:
        if v[0] > k:
            return v[0] - k
        else:
            return 0
n, k = [int(x) for x in input().split()]
v = [int(x) for x in input().split()]
print(fun(v, n, k))
