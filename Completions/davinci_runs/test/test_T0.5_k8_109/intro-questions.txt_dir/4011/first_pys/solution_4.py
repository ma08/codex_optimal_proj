

import sys

def solve(a, f):
    n = len(a)
    d = [0 for i in range(n)]
    for i in range(n):
        d[i] = f[int(a[i]) - 1]
    d.append(0)
    f[0] = -1
    f[8] = -1
    for i in range(n):
        if d[i] == d[i + 1]:
            d[i] = f[d[i] - 1]
    return int(''.join(map(str, d[:-1])))

def main():
    n = int(sys.stdin.readline())
    a = sys.stdin.readline().strip()
    f = list(map(int, sys.stdin.readline().split()))
    print(solve(a, f))


if __name__ == "__main__":
    main()