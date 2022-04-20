n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [0]*n
if n == 1:
    print("YES")
    print(1)
    exit()
if k == 1:
    if a.count(a[0]) == n:
        print("YES")
        print(*b)
    else:
        print("NO")
    exit()
if a.count(a[0]) == n:
    print("YES")
    for i in range(n):
        if i == 0:
            b[i] = 1
        else:
            b[i] = 2
    print(*b)
    exit()
if a.count(a[0]) == n - 1:
    if a[0] in a[1:]:
        print("YES")
        for i in range(n):
            if i == 0:
                b[i] = 2
            else:
                b[i] = 1
        print(*b)
    else:
        print("NO")
    exit()
if a.count(a[0]) == n - 2:
    if a[0] not in a[2:]:
        if a[1] in a[2:]:
            print("YES")
            for i in range(n):
                if i == 0 or i == 1:
                    b[i] = 1
                else:
                    b[i] = 2
            print(*b)
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")

