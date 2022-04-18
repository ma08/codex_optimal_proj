t = int(input())
for i in range(t):
    n = int(input())
    a = []
    for j in range(n):
        a.append(int(input()))
    a.sort()
    s1 = 0
    s2 = 0
    for k in range(len(a)):
        if k < len(a) / 2:
            s1 += a[k]**2
        else:
            s2 += a[k]
    print(s1 * s2)
