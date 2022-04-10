
n, k = map(int, input().split())

if n == 1:
    print("YES")
    print("1")
elif n > 2 * (2 ** (k - 1) - 1) or n < 2 ** (k - 1) or n == 2 ** (k - 1):
    print("NO")
else:
    print("YES")
    for i in range(k - 1):
        print(2 ** (k - i - 1) - 1, end=' ')

    if n - (2 ** (k - 1) - 1) == 2 ** (k - 1):
        print(2 ** (k - 1))
    else:
        print(n - (2 ** (k - 1) - 1))
