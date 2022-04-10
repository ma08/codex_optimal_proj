
n, m, d = map(int, input().split())
c = list(map(int, input().split()))

if sum(c) > n or max(c) > d or d == 1 or (m == 1 and c[0] == 1) or (m == 1 and c[0] > 1) or (m == 2 and c[0] == 1 and c[1] == 1):
    print('NO')
    exit()

print('YES')

i = 0
while i < n:
    if m == 0:
        print('0 ' * (n - i), end='')
        break
    if c[0] > d:
        print('0 ' * d + '1 ' * (c[0] - d), end='')  # 1
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
        print('0 ' * (d - 1) + '2 ' * (c[0] - d + 1), end='')  # 2
        i += c[0]
    else:
        print('2 ' * c[0], end='')
        i += c[0]
    c.pop(0)
    m -= 1
