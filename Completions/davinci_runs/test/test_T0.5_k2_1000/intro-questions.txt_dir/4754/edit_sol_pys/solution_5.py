

import sys
import collections

def main():
    n = int(sys.stdin.readline())
    socks = map(int, sys.stdin.readline().split())
    sock_count = collections.Counter(socks)
    if any(sock_count[x] % 2 for x in sock_count):  # if any of the socks are odd
        print("impossible")
    else:
        print(sum(sock_count[x]/2 - 1 for x in sock_count))  # if all socks are even

if __name__ == "__main__":
    main()
