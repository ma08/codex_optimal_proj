

import sys

def main():
    n, k = [int(x) for x in sys.stdin.readline().strip().split()]
    s = sys.stdin.readline().strip()
    if n < k:
        print -1
        return
    if n == k:
        print 0
        return
    if n > k:
        print n - k
        return

if __name__ == '__main__':
    main()