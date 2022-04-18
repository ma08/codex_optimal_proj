#!/usr/bin/env python3

import math

def main():
    for i in range(int(input())):
        x = float(input())
        print(int(math.ceil(x * 1000 * (5280/4854))))

if __name__ == "__main__":
    main()
