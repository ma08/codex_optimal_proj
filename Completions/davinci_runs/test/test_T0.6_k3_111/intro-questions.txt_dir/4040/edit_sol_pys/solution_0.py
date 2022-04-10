
n, m, d = map(int, input().split())  # n: number of soldiers, m: number of groups, d: distance
c = list(map(int, input().split()))  # c[i]: number of soldiers in group i

if sum(c) > n or max(c) > d or d == 1 or (m == 1 and c[0] == 1) or (m == 1 and c[0] > 1):  # impossible
    print('NO')
    exit()

print('YES')

for i in range(n):
    if i % 2 == 0:
        print(1, end=' ')
        c[0] -= 1
        if c[0] == 0:
            c.pop(0)
            m -= 1
    else:
        print(2, end=' ')
        c[1] -= 1
        if c[1] == 0:
            c.pop(1)
            m -= 1
    if m == 0:  # all groups are used
        print('0 ' * (n - i - 1), end='')
        exit()
