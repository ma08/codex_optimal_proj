

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    a = [a[i][j] for i in range(n) for j in range(m)]
    if a == sorted(a):
        print("YES")
        print("0 " * n)
        print("0 " * m)
    else:
        print("NO")

if __name__ == "__main__":
    main()
