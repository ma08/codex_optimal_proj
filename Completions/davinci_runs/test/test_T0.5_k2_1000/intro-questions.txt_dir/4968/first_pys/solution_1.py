

import sys

def main():
    n, s, r = (int(x) for x in sys.stdin.readline().split())
    damaged = set(int(x) for x in sys.stdin.readline().split())
    reserve = set(int(x) for x in sys.stdin.readline().split())
    print(max(0, s - len(reserve.intersection(damaged.union({x - 1 for x in damaged}).union({x + 1 for x in damaged})))))

if __name__ == "__main__":
    main()