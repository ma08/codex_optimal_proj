

import sys

def main():
    x, k, d = map(int, sys.stdin.readline().rstrip().split())
    if abs(x) < k * d:  # k回以下
        print(abs(x - (x // d) * d))
    else:  # k回以上
        print(abs(x) - (k * d))

if __name__ == '__main__':
    main()
