

import sys

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]

    a = []
    for i in range(n):
        a.append([int(x) for x in sys.stdin.readline().split()])

    r = [0]*n
    c = [0]*m

    for i in range(n):
        zero = 0
        one = 0
        for j in range(m):
            if a[i][j] == 0:
                zero += 1
            else:
                one += 1
        if zero > one:
            r[i] = 1

    for j in range(m):
        zero = 0
        one = 0
        for i in range(n):
            if a[i][j] == 0:
                zero += 1
            else:
                one += 1
        if zero > one:
            c[j] = 1

    for i in range(n):
        for j in range(m):
            if r[i] == 1:
                a[i][j] = 1 - a[i][j]
            if c[j] == 1:
                a[i][j] = 1 - a[i][j]

    sorted_ = True
    for i in range(n):
        for j in range(m-1):
            if a[i][j] > a[i][j+1]:
                sorted_ = False

    if sorted_:
        print("YES")
        print("".join([str(x) for x in r]))
        print("".join([str(x) for x in c]))
    else:
        print("NO")

if __name__ == '__main__':
    main()
