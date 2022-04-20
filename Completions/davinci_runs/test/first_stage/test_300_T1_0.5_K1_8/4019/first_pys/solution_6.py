

import sys

def main():
    n, m, d = map(int, sys.stdin.readline().split())
    edges = [sys.stdin.readline().split() for _ in range(m)]
    if d == 0:
        if n == 2:
            print("YES")
            print("1 2")
        else:
            print("NO")
    elif d == 1:
        if n == 2:
            print("NO")
        else:
            print("YES")
            for i in range(2, n + 1):
                print(1, i)
    elif d == n - 1:
        if n == 2:
            print("YES")
            print("1 2")
        else:
            print("YES")
            for i in range(2, n):
                print(i, i + 1)
    elif d == n - 2:
        if n == 3:
            print("NO")
        else:
            print("YES")
            for i in range(2, n):
                print(i, i + 1)
            print(1, n)
    else:
        print("NO")

if __name__ == '__main__':
    main()