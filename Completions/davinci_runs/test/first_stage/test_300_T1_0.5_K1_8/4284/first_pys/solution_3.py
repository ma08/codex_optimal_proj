

import sys

def main():
    q = int(sys.stdin.readline().strip())
    for _ in range(q):
        k, n, a, b = map(int, sys.stdin.readline().strip().split())
        if k >= a*n:
            print(n)
            continue
        if k < b*n:
            print(-1)
            continue
        print(int(k/a))

if __name__ == '__main__':
    main()