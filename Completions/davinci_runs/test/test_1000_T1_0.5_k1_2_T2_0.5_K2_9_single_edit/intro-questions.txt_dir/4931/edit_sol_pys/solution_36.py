

import sys

def main():
    x, y = map(int, sys.stdin.readline().split())
    print(x / (y - 1) if x != 0 else "ALL GOOD" if y == 1 else "IMPOSSIBLE")

if __name__ == "__main__":
    main()
