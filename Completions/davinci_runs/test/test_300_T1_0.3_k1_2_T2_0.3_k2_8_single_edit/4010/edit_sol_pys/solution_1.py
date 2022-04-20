
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
    for i in d.values():
        if len(i) > 2:
            for j in range(len(i)-2):
                if i[j+2] - i[j] > 1:
                    flag = True
                    break
            if flag:
                break
    if flag:
        print("YES")
    else:
        print("NO")
