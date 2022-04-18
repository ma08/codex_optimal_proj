#!/usr/bin/env python3

import sys

def main():
    N = int(sys.stdin.readline())
    wait_time = []
    for i in range(N):
        M, S = map(int, sys.stdin.readline().split())
        wait_time.append(S/M)
    print(sum(wait_time)/N)

if __name__ == "__main__":
    main()
