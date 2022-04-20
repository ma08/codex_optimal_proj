
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]].append(i)
        else:
            d[a[i]] = [i]
    flag = False
    for i in d:
        if len(d[i]) > 3:
            for j in range(len(d[i])-3):
                if d[i][j+3] - d[i][j] > 2:
                    flag = True
                    break
            if flag:
                break
    if flag:
        print("YES")
    else:
        print("NO")
