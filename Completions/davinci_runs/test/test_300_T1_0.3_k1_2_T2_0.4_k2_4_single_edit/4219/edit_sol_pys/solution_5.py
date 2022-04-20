# -*- coding: utf-8 -*-
# AtCoder Beginner Contest
# Problem B

import sys

def main():
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A + B if A + B < 10 else 'error')

if __name__ == "__main__":
    main()
