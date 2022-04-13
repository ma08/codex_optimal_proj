#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    temperatures = sorted(map(int, sys.stdin.readline().split()))
    if temperatures[0] == temperatures[1] or temperatures[-2] == temperatures[-1] or temperatures[-2] - temperatures[1] > temperatures[-1] - temperatures[0]:
        print("impossible")
        return
    print(" ".join(map(str, reversed(temperatures))))

if __name__ == "__main__":
    main()
