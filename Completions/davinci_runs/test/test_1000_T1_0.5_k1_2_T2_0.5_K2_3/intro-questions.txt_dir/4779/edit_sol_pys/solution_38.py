

def max_sum(a):
    a.sort()
    s1 = 0
    s2 = 0
    for i in range(len(a)):
        if i < len(a) / 2:
            s1 += a[i]**2
        else:
            s2 += a[i]

    return s1 * s2


print(max_sum([1, 2, 3, 4]))
