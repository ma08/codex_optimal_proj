

n, k = map(int, input().split())

if n < k:
    print("NO")
elif n == k:
    print("YES")
    for i in range(1, n + 1):
        print(i, i)
elif n > k and n % 2 == 0:
    print("YES")
    a = []
    for i in range(1, n + 1):
        a.append(i)

    for i in range(0, n, 2):
        if i == 0:
            print(a[i], a[i + 1])
        elif i == n - 2:
            print(a[i + 1], a[i])
        else:
            print(a[i + 1], a[i])
elif n % 2 == 1 and n > k:
    print("YES")
    a = []
    for i in range(1, n + 1):
        a.append(i)

    for i in range(0, n - 1, 2):
        if i == 0:
            print(a[i], a[i + 1])
        elif i == n - 2:
            print(a[i + 1], a[i])
        else:
            print(a[i + 1], a[i])
    print(a[n - 1], a[n - 1])