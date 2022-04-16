

import sys
import collections

def main():
    n = int(sys.stdin.readline())
    socks = map(int, sys.stdin.readline().split())
    sock_count = collections.Counter(socks)
    if any(sock_count[x] % 2 != 0 for x in sock_count):
        print("impossible")
    else:
        print(sum((sock_count[x]/2) - 1 for x in sock_count))

if __name__ == "__main__":
    main()
