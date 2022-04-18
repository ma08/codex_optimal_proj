

import sys
import collections

def main():
    n = int(sys.stdin.readline())
    words = sys.stdin.read().splitlines()
    counts = collections.Counter(words)
    for word, count in counts.items():
        print(word, count)

if __name__ == '__main__':
    main()
