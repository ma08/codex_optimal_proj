#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline().strip())
    recited = [int(sys.stdin.readline().strip()) for _ in range(n)]
    missing = set()
    for i in range(1, recited[-1] + 1):
        if i not in recited:
            missing.add(i)
    if len(missing) > 0:
        for m in missing:
            print(m)
    else:
        print("good job")

if __name__ == "__main__":
    main()
