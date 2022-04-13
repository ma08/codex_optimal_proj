#! /usr/bin/env python3

import sys

def main():
    N = int(sys.stdin.readline().strip())
    print(1 - (N - 1)/N, end='\n')

if __name__ == "__main__":
    main()
