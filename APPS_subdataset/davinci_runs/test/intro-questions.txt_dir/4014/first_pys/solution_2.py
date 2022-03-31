

import sys

def solve(n, m, s, d, c):
    # print('\n\nn={}, m={}'.format(n, m))
    # print('s={}, d={}, c={}'.format(s, d, c))
    # print('\n')

    days = [0]*n
    for i in range(m):
        for j in range(s[i], d[i]):
            days[j] = 1

    # print('days={}'.format(days))

    for i in range(m):
        for j in range(s[i], d[i]):
            days[j] = 2
            c[i] -= 1
            if c[i] == 0:
                break

    # print('days={}'.format(days))

    for i in range(m):
        if c[i] > 0:
            return -1

    for i in range(n):
        if days[i] == 1:
            days[i] = m+1

    # print('days={}'.format(days))
    return days


def main():
    n, m = [int(x) for x in input().split()]

    s = []
    d = []
    c = []

    for i in range(m):
        si, di, ci = [int(x) for x in input().split()]
        s.append(si-1)
        d.append(di)
        c.append(ci)

    days = solve(n, m, s, d, c)

    if days == -1:
        print(-1)
    else:
        print(' '.join([str(d) for d in days]))

if __name__ == '__main__':
    main()