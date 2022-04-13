

import sys
import collections

def main():
    n = int(sys.stdin.readline())
    socks = map(int, sys.stdin.readline().split())
    sock_counts = collections.Counter(socks)
    if any(sock_counts[x] % 2 != 0 for x in sock_counts):
        print("impossible")
    else:
        print(sum(sock_counts[x]/2 - 1 for x in sock_counts))

if __name__ == "__main__":
    main()
