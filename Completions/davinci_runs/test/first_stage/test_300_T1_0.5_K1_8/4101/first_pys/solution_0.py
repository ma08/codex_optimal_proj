

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
    r = [0] * n
    c = [0] * m
    for i in range(n):
        if a[i][0] == 1:
            r[i] = 1
    for j in range(1, m):
        if a[0][j] == 1:
            c[j] = 1
    for i in range(1, n):
        for j in range(1, m):
            if a[i][j] == 1:
                if r[i] == 1 and c[j] == 1:
                    print("NO")
                    return
                if r[i] == 0 and c[j] == 0:
                    print("NO")
                    return
                if r[i] == 0:
                    c[j] = 1
                else:
                    r[i] = 1
    print("YES")
    print("".join(map(str, r)))
    print("".join(map(str, c)))

main()