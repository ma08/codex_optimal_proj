

import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().strip().split())
    max_x = max(a, c)
    min_y = min(b, d)
    print(max_x*min_y)

if __name__ == "__main__":
    main()