

import sys

def main():
    n, r = map(int, sys.stdin.readline().split())
    r = [0]
    for line in sys.stdin:
        a, b = map(int, line.split())
        r.append(max(r[-1] - (a - r[-1]), 0) + b)
    print(len(r) - 1)

if __name__ == "__main__":
    main()
