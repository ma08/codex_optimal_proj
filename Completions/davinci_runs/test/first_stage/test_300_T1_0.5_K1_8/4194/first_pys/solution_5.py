

import sys
import heapq


def main():
    n, m = map(int, sys.stdin.readline().split())
    assignments = list(map(int, sys.stdin.readline().split()))
    assignments.sort()
    days_hanging_out = 0
    for a in assignments:
        if n < a:
            print(-1)
            sys.exit()
        days_hanging_out += n - a
        n -= a
    print(days_hanging_out)


if __name__ == '__main__':
    main()