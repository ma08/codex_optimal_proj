

import sys

def main():
    x, y = map(int, sys.stdin.readline().split())
    if x == 0:
        print("ALL GOOD") if y == 1 else print("IMPOSSIBLE") #if not used in a way that makes sense
    else:
        print(x / (y - 1))

if __name__ == "__main__":
    main()
