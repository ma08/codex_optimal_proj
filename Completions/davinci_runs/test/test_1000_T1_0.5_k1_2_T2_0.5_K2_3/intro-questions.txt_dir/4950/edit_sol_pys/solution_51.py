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
    n = int(input('Enter number of photos: '))
    speeds = []
    for _ in range(n):
        t, d = map(int, input('Enter time and distance: ').split())
        speeds.append(d / t)
    print(int(max(speeds)))

if __name__ == "__main__":
    main()
