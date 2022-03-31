
n, m, d = map(int, input().split())
c = list(map(int, input().split()))

if sum(c) > n:
    print('NO')
    exit()

if m == 1:
    if d < n:
        print('NO')
        exit()
    else:
        print('YES')
        print(*[0] * n)
        exit()

if m == 2:
    if d < n - c[0]:
        print('NO')
        exit()
    else:
        print('YES')
        print(*([0] * c[0] + [1] * c[1]), sep=' ')
        exit()

if m == 3:
    if d < n - c[0] - c[1]:
        print('NO')
        exit()
    else:
        print('YES')
        print(*([0] * c[0] + [1] * c[1] + [2] * c[2]), sep=' ')
        exit()

if m == 4:
    if d < n - c[0] - c[1] - c[2]:
        print('NO')
        exit()
    else:
        print('YES')
        print(*([0] * c[0] + [1] * c[1] + [2] * c[2] + [3] * c[3]), sep=' ')
        exit()

print('NO')
