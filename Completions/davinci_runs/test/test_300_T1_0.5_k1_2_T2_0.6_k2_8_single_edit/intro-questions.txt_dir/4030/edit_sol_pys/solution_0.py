
n = int(input())
s = input()

if n == 2:
    if s[0] >= s[1]:
        print(1)
        print(1)
    else:
        print(2)
        print(1, 2)

else:
    if s[-1] < s[-2]:
        c = [1] * n
        c[-1] = 2
    else:
        c = [1] * n

    for i in range(1, n - 1):
        if s[i] > s[i + 1]:
            c[i] = max(c[i], c[i + 1])
            c[i + 1] = max(c[i], c[i + 1])
        if s[i] < s[i - 1]:
            c[i] = max(c[i], c[i - 1])
            c[i - 1] = max(c[i], c[i - 1])

    if s[0] >= s[1]:
        c[0] = max(c[0], c[1])
        c[1] = max(c[0], c[1])

    if s[0] > s[1]:
        print(2)
        print(1, 2)

    print(max(c))
    print(*c)
