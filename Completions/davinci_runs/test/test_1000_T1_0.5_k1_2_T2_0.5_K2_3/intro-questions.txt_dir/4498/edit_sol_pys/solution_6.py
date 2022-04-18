#!/usr/bin/env python3
import sys

def main():
    x, y, z = [int(i) for i in sys.stdin.readline().split()]
    print(z, x, y)

if __name__ == "__main__":
    main()
