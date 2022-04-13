

n, m = map(int, input().split())

if n > m:
    print('Dr. Chaz needs {} more piece{} of chicken!'.format(n - m, 's' if (n - m) > 1 else ''))
else:
    print('Dr. Chaz will have {} piece{} of chicken left over!'.format(m - n, 's' if (m - n) > 1 else ''))
