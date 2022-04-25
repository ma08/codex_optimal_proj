


# https://www.hackerrank.com/challenges/picking-numbers

import sys

def main():
    n = int(sys.stdin.readline())
    a = map(int, sys.stdin.readline().split())[:n]
    freq = [0] * 100

    for i in a:
        freq[i] += 1

    # print freq

    m = 0
    for i in range(n-1):
        m = max(m, freq[i] + freq[i+1])

    print m

if __name__ == "__main__":
    main()
