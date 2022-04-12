

import sys
import collections

def main():
    n = int(sys.stdin.readline())
    verdict = sys.stdin.read().split()
    count = collections.Counter(verdict)
    for verdict, count in count.items():
        print(verdict, "x", count)

if __name__ == '__main__':
    main()
