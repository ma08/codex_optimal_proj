

n, m, d = map(int, input().split())
c = list(map(int, input().split()))

if sum(c) > n:
    print('NO')
    exit()

if max(c) > d:
    print('NO')
    exit()

if d == 1:
    print('NO')
    exit()

if m == 1 and c[0] == 1:
    print('YES')
    print('0 ' * n)
    exit()

if m == 1 and c[0] > 1:
    print('YES')
    print('0 ' * (n - c[0]) + '1 ' * c[0])
    exit()

print('YES')

i = 0
while i < n:
    if m == 0:
        print('0 ' * (n - i), end='')
        break
    if c[0] > d:
        print('0 ' * d + '1 ' * (c[0] - d), end='')
        i += c[0]
    else:
        print('1 ' * c[0], end='')
        i += c[0]
    c.pop(0)
    m -= 1
    if m == 0:
        print('0 ' * (n - i), end='')
        break
    if c[0] > d:
        print('0 ' * (d - 1) + '2 ' * (c[0] - d + 1), end='')
        i += c[0]
    else:
        print('2 ' * c[0], end='')
        i += c[0]
    c.pop(0)
    m -= 1