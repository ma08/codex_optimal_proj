#!/usr/bin/env python3

def main():
    """
    input:
        n: number of photos
        t: time in hours
        d: distance in miles
    output:
        max speed in mph
    """
    n = int(raw_input())
    speeds = []
    for _ in range(n):
        t, d = map(int, raw_input().split())
        speeds.append(d / t)
    print int(max(speeds))

if __name__ == "__main__":
    main()
