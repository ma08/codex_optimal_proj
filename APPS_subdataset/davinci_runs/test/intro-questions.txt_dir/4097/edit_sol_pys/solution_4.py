#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    if n == 2:
        print(0)
        return
    diff = a[1] - a[0]
    for i in range(2, n):
        if a[i] - a[i-1] != diff:
            if a[i] - a[i-1] == diff + 1:
                if a[i-1] - a[i-2] == diff - 1:
                    a[i-1] -= 1
                    print(1)
                    return
                else:
                    a[i] -= 1
                    print(1)
                    return
            elif a[i] - a[i-1] == diff - 1:
                if a[i-1] - a[i-2] == diff + 1:
                    a[i] += 1
                    print(1)
                    return
                else:
                    a[i-1] += 1
                    print(1)
                    return
            else:
                print(-1)
                return
    print(0)

if __name__ == "__main__":
    main()
