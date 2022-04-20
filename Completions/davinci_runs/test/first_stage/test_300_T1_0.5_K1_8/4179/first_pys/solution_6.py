

import sys

def main():
    n, m, c = map(int, sys.stdin.readline().split())
    b = list(map(int, sys.stdin.readline().split()))
    a = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

    ans = 0
    for i in range(n):
        if sum([a[i][j] * b[j] for j in range(m)]) + c > 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()