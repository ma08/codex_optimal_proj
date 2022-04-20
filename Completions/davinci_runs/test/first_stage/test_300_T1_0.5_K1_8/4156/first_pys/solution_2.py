

n, w = map(int, input().split())
a = list(map(int, input().split()))

if n == 1:
    print(w+1)
else:
    d = {}
    d[0] = 1
    for i in range(1, n):
        d2 = {}
        for k in d.keys():
            if k+a[i] > w or k+a[i] < 0:
                continue
            if k+a[i] in d2.keys():
                d2[k+a[i]] += d[k]
            else:
                d2[k+a[i]] = d[k]
        d = d2
    print(sum(d.values()))