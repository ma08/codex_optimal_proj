

n, d, k = map(int, input().split())

if d == 1:
    print("YES")
    for i in range(2, n+1):
        print(1, i)
elif d == 2:
    if k >= n - 1:
        print("YES")
        for i in range(2, n+1):
            print(1, i)
    else:
        print("NO")
elif d == 3:
    if k >= n - 1:
        print("YES")
        for i in range(2, n+1):
            print(1, i)
    elif k >= n / 2:
        print("YES")
        print("3 1")
        for i in range(4, n+1):
            print(1, i)
    else:
        print("NO")
elif d == 4:
    if k >= n - 1:
        print("YES")
        for i in range(2, n+1):
            print(1, i)
    elif k >= n / 2:
        print("YES")
        print("3 1")
        for i in range(4, n+1):
            print(1, i)
    elif k >= n / 3:
        print("YES")
        print("3 1")
        print("4 3")
        for i in range(5, n+1):
            print(1, i)
    else:
        print("NO")
elif d == 5:
    if k >= n - 1:
        print("YES")
        for i in range(2, n+1):
            print(1, i)
    elif k >= n / 2:
        print("YES")
        print("3 1")
        for i in range(4, n+1):
            print(1, i)
    elif k >= n / 3:
        print("YES")
        print("3 1")
        print("4 3")
        for i in range(5, n+1):
            print(1, i)
    elif k >= n / 4:
        print("YES")
        print("3 1")
        print("4 3")
        print("5 3")
        for i in range(6, n+1):
            print(1, i)
    else:
        print("NO")
elif d == 6:
    if k >= n - 1:
        print("YES")
        for i in range(2, n+1):
            print(1, i)
    elif k >= n / 2:
        print("YES")
        print("3 1")
        for i in range(4, n+1):
            print(1, i)
    elif k >= n / 3:
        print("YES")
        print("3 1")
        print("4 3")
        for i in range(5, n+1):
            print(1, i)
    elif k >= n / 4:
        print("YES")
        print("3 1")
        print("4 3")
        print("5 3")
        for i in range(6, n+1):
            print(1, i)
    elif k >= n / 5:
        print("YES")
        print("3 1")
        print("4 3")
        print("5 3")
        print("6 3")
        for i in range(7, n+1):
            print(1, i)
    else:
        print("NO")