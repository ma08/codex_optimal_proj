

import sys

def main():
    q = int(sys.stdin.readline())
    for _ in range(q):
        k, n, a, b = map(int, sys.stdin.readline().split())
        print(max(0, min((k - a) // (a - b) + 1, n)))

if __name__ == "__main__":
    main()
