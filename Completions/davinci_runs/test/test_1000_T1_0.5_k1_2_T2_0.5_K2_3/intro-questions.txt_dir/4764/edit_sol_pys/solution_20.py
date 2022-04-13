

import sys

def main():
    n, h, v = map(int, input().split())
    print(4 * (n - h) * (n - v))

if __name__ == "__main__":
    main()
