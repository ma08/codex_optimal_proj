
n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == 1:
    print("YES")
    print(" ".join(map(str, [1]*n)))
else:
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]].append(i)
        else:
            d[a[i]] = [i]

    if len(d) > k:
        print("NO")
    else:
        c = [0]*n
        for i in range(len(d)):
            for j in range(len(d[a[i]])):
                c[d[a[i]][j]] = i+1
        print("YES")
        print(" ".join(map(str, c)))
