#!/usr/bin/python3

import sys

def main():
    s = sys.stdin.readline().strip()
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    cnt = 0
    for v in d.values():
        if v % 2 != 0:
            cnt += 1
    print(cnt - 1 if cnt != 0 else 0)

if __name__ == "__main__":

    main()
