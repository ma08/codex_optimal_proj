

import sys

def main():
    t = int(sys.stdin.readline().strip())

    for _ in range(t):
        n, m = map(int, sys.stdin.readline().strip().split())
        a = [0] * (n - 1) + [m]
        print(sum(abs(a[i] - a[i + 1]) for i in range(n - 1)))

if __name__ == '__main__':
    main()