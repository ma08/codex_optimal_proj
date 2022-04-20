

import sys

def main():
    n, r = map(int, sys.stdin.readline().split())
    r = [r] * (n + 1)
    for line in sys.stdin:
        a, b = map(int, line.split())
        r[a] = max(r[a], b)
    print(r.index(0))

if __name__ == "__main__":
    main()
