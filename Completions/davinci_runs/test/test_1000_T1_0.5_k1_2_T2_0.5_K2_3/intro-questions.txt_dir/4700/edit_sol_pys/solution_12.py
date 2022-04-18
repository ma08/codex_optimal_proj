

import collections
import sys

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(m)]

    print(n, m)
    print(h)
    print(ab)

if __name__ == '__main__':
    main()
