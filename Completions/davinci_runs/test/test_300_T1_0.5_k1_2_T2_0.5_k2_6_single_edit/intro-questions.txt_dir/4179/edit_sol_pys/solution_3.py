

import sys

def main():
    n, m, c = map(int, sys.stdin.readline().split())
    b = list(map(int, sys.stdin.readline().split()))
    a = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
    for i in range(n):
        print(sum(a[i][j]*b[j] for j in range(m)) + c)

if __name__ == "__main__":
    main()
