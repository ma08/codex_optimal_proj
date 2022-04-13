

import sys

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        x, y = [int(i) for i in sys.stdin.readline().split()]
        if y == 1:
            print("IMPOSSIBLE")
        elif x == 0:
            print("ALL GOOD")
        else:
            print(int(x / (y - 1)))

if __name__ == "__main__":
    main()
