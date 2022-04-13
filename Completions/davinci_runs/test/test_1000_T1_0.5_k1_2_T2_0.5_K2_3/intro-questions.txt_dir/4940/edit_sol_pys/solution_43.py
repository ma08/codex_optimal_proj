
#!/usr/bin/env python3

import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    p = []
    for i in range(N):
        p.append(list(map(int, sys.stdin.readline().split())))

    # the time a swather is completed
    t = [0] * N

    # the time stage j is completed
    s = [0] * M

    # the number of swathers completed at stage j
    c = [0] * M

    # the number of swathers completed
    d = 0

    # the swathers completing at stage j
    e = [[] for i in range(M)]

    for i in range(N):
        for j in range(M):
            if i == 0:
                s[j] = p[0][j]
            else:
                if j == 0:
                    s[j] = s[j] + p[i][j]
                elif c[j-1] == 0:
                    s[j] = s[j] + p[i][j]
                else:
                    s[j] = max(s[j], e[j-1][0]) + p[i][j]

            if j == M-1:
                t[i] = s[j]
            c[j] += 1
            e[j].append(t[i])
            if j > 0:
                e[j-1].pop(0)
            d += 1

    print(' '.join(map(str, t)))

if __name__ == '__main__':
    main()
