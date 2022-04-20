
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = dict()
    for i in range(n):
        if a[i] in d:
            d[a[i]].append(i)
        else:
            d[a[i]] = []
            d[a[i]].append(i)
    flag = False
    for i in d:
        if len(d[i]) > 2:
            if d[i][2] - d[i][0] > 1:
                flag = True
                break
            if flag:
                break
    if flag:
        print("YES")
    else:
        print("NO")
