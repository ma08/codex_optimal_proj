def get_sum(a, i):
    res = 0
    while i > 0:
        res += a[i]
        i -= i & -i
    return res

def update(a, i, delta):
    while i < len(a):
        a[i] += delta
        i += i & -i

def get_min(a, i):
    res = i
    while i < len(a):
        if a[i] < a[res]:
            res = i
        i += i & -i
    return res

a = [1, 2, 3, 4, 5, 6]
update(a, 2, 1)
print(a)
print(get_sum(a, 5))
print(get_min(a, 1))
