

n, m = [int(x) for x in input().split()]
s = []
d = []
c = []
for i in range(m):
    si, di, ci = [int(x) for x in input().split()]
    s.append(si)
    d.append(di)
    c.append(ci)

def isPossible(s, d, c, n, m):
    a = [0] * n
    for i in range(m):
        if c[i] > d[i] - s[i]:
            return False
        for j in range(s[i], d[i]):
            if a[j] != 0:
                return False
            a[j] = i + 1
    return True

def printSchedule(s, d, c, n, m):
    a = [0] * n
    for i in range(m):
        for j in range(s[i], s[i] + c[i]):
            a[j] = i + 1
        a[d[i] - 1] = m + 1
    print(*a)

if not isPossible(s, d, c, n, m):
    print(-1)
else:
    printSchedule(s, d, c, n, m)