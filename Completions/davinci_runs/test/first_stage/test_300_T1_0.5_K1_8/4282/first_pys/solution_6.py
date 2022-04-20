

import sys

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    p = [0] * n
    p[0] = 1
    p[1] = a[0][0]
    p[2] = a[0][1]
    for i in range(3, n):
        if a[p[i - 1] - 1][0] == p[i - 2]:
            p[i] = a[p[i - 1] - 1][1]
        else:
            p[i] = a[p[i - 1] - 1][0]
    print(*p)

if __name__ == "__main__":
    main()