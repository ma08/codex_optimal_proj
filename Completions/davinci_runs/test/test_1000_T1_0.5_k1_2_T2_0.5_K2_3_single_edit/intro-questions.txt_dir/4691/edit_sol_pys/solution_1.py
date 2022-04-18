

import sys
import collections

def main():
    n = int(sys.stdin.readline())
    verdicts = sys.stdin.read().strip().split()
    counts = collections.Counter(verdicts)
    for verdict, count in counts.items():
        print(verdict, "x", str(count))

if __name__ == '__main__':
    main()
