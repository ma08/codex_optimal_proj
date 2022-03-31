
# TODO: WA (not solved)
# TODO: WA (not solved)

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    c = []
    d = []
    e = []
    for i in range(n):
        if i == 0:
            b.append(a[i])
        elif i == 1:
            b.append(a[i])
            if a[i] == a[i-1]:
                c.append([a[i-1], a[i]])
        else:
            b.append(a[i])
            if a[i] == a[i-1]:
                c.append([a[i-1], a[i]])
            if a[i] == a[i-2]:
                d.append([a[i-2], a[i-1], a[i]])
            if a[i] == a[i-3]:
                e.append([a[i-3], a[i-2], a[i-1], a[i]])
    if len(c) > 0 or len(d) > 0 or len(e) > 0:
        print("YES")
    else:
        print("NO")
