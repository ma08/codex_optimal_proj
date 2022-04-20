

import sys

def main():
    q = int(sys.stdin.readline())
    for _ in range(q):
        k, n, a, b = map(int, sys.stdin.readline().split())
        if a <= b:
            print(-1)
            continue
        print((k - b - 1) // (a - b))

if __name__ == "__main__":
    main()
