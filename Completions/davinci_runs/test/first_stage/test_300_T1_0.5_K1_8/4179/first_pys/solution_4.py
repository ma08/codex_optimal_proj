

import sys

def main():
    n, m, c = map(int, sys.stdin.readline().split())
    b = list(map(int, sys.stdin.readline().split()))
    a = []
    for i in range(n):
        a.append(list(map(int, sys.stdin.readline().split())))

    count = 0
    for i in range(n):
        s = 0
        for j in range(m):
            s += a[i][j] * b[j]
        if s + c > 0:
            count += 1

    print(count)

if __name__ == '__main__':
    main()