#!/usr/bin/python3

import sys

def main():
    vals = [int(x) for x in sys.stdin.readline().split()]
    out = 0
    for i in range(8):
        out += 19 - vals[i]
    print(out)

main()
