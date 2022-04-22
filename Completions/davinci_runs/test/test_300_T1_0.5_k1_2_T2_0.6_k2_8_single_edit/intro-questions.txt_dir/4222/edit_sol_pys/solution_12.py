#

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    victim = set([i for i in range(1, n+1)])
    for _ in range(k):
        d = int(sys.stdin.readline())
        victim -= set(map(int, sys.stdin.readline().split()))
    print(len(victim))

if __name__ == '__main__':
    main()
