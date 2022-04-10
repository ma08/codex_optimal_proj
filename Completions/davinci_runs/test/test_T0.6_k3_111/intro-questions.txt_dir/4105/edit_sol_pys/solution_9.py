n, k = map(int, input().split())
if k == 2:
    print("YES")
    for i in range(n):
        print(1, 2)
else:
    if n % 2 == 0:
        print("YES")
        for i in range(1, n // 2 + 1):
            print(i, k - i + 1)
        for i in range(1, n // 2 + 1):
            print(k - i + 1, i)
    else:
        print("YES")
        for i in range(1, n // 2 + 1):
            print(i, k - i + 1)
        print(k // 2 + 1, k // 2 + 1)
        for i in range(1, n // 2 + 1):
            print(k - i + 1, i)
