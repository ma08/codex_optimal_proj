#!/usr/bin/env python

import sys

def main():
    s = sys.stdin.readline().strip()
    K = int(sys.stdin.readline().strip())
    print(sorted(set(s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)))[K-1], end='')

if __name__ == "__main__":
    main()
