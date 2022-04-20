
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
    flag = 0
    for i in d:
        if len(d[i]) > 2:
            for j in range(len(d[i])-2):
                if d[i][j+2] - d[i][j] > 1:
                    flag = 1
                    break
            if flag:
                break
    if flag == 1:
        print("YES")
    else:
        print("NO")
