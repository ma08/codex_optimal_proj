import collections

import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))

    cnt = collections.Counter(a)

    ans = 0
    for v in cnt.values():
        if v > 2:
            ans += v - 2

    print(m)

if __name__ == '__main__':
    main()
