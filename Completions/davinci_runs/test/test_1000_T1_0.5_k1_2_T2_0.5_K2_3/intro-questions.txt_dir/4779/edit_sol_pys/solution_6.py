

def max_sum(a, b):
    a.sort()
    s1 = 0
    for i in range(len(a)):
        if i < len(a) / 2:
            s1 += a[i]**2
    for i in range(len(b)):
        if i < len(b) / 2:
            s2 += b[i]**2
    return s1 * s2

    return s1 * s2


print(s1 * s2)
