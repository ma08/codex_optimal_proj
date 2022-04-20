

import sys

def main():
    n, m, d = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, sys.stdin.readline().split())))
    if d == 0:
        print("YES")
        for i in range(2, n + 1):
            print(1, i)
        return
    if d == n - 1:
        print("YES")
        for i in range(1, n):
            print(i, i + 1)
        return
    if d == 1:
        for i in range(2, n + 1):
            if (1, i) in edges:
                print("YES")
                print(1, i)
                for j in range(1, n + 1):
                    if j != i:
                        print(j, 1)
                return
        print("NO")
        return

if __name__ == '__main__':
    main()