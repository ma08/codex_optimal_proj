#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    times = []
    distances = []
    for i in range(n):
        [t, d] = [int(x) for x in sys.stdin.readline().split()]
        times.append(t)
        distances.append(d)
    #print(times)
    #print(distances)
    speeds = [0 for x in range(n)]
    for i in range(n-1):
        speeds[i] = (distances[i+1] - distances[i]) / (times[i+1] - times[i])
    #print(speeds)
    print(int(max(speeds))) 

if __name__ == '__main__':
    main()
