

import sys

def main():
    n, m, d = map(int, sys.stdin.readline().split())
    edges = []
    for i in range(m):
        edges.append(tuple(map(int, sys.stdin.readline().split())))
    if d == 0:
        print("YES")
        for i in range(1, n):
            print(i, i + 1)
    elif d == n - 1:
        print("YES")
        for i in range(2, n):
            print(1, i)
    else:
        print("NO")

if __name__ == "__main__":
    main()