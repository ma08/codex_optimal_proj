#!/usr/bin/env python3

import sys

def main():
    input_line = sys.stdin.readline()
    N = float(input_line.strip())
    print(pow(N, 1.0 / N))

if __name__ == "__main__":
    main()
