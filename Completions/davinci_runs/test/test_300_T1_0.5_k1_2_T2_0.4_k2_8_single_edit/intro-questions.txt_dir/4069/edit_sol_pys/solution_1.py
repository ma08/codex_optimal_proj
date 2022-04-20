

import sys

def main():
    x, k, d = map(int, input().split())
    if abs(x) < k * d:
        print(abs(x - (x // d) * d))
    else:
        print(abs(x) - (k * d))

if __name__ == '__main__':
    main()
