

import sys

def main():
    x, y, z = map(int, sys.stdin.readline().split())
    if x == 0 and y == 0:
        print("ALL GOOD" if z == 1 else "IMPOSSIBLE")
    else:
        print(x / (y - z))

if __name__ == "__main__":
    main()
