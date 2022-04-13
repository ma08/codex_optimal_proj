

def coconut(n, s, k):
    l = list(range(1, n + 1))
    i = 0
    while len(l) > 1:
        i += s - 1
        i %= len(l)
        l.pop(i)
    return l[0]

print(coconut(int(input()), int(input()), int(input())))
