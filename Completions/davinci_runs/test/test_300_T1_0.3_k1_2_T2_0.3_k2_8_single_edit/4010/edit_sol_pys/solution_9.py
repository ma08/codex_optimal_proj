
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = dict()
    for i in range(n):
        if a[i] in d:
            d[a[i]].append(i)
        else:
            d[a[i]] = list()
            d[a[i]].append(i)
    flag = False
    for i in d:
        if len(d[i]) > 2:
            for j in range(len(d[i])-2):
                if d[i][j+2] - d[i][j] > 1:
                    flag = True
                    break
            if flag:
                break
    if flag:
        print("YES")
    else:
        print("NO")
