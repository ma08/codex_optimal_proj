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
    n = int(input())
    maxspeed = 0
    for _ in range(n):
        t, d = map(int, input().split())
        speed = d / t
        if speed > maxspeed:
            maxspeed = speed
    print(int(maxspeed))

if __name__ == "__main__":
    main()
