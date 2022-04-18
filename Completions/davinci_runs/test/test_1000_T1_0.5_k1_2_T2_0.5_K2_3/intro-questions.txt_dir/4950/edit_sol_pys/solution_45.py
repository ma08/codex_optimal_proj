#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    times = [0] * n
    distances = [0] * n
    for i in range(n):
        times[i], distances[i] = [float(x) for x in sys.stdin.readline().split()] #read in the data

    max_speed = 0
    for i in range(n):
        for j in range(i+1, n):
            time_diff = times[j] - times[i]
            dist_diff = distances[j] - distances[i] #calculate the distance and time difference
            speed = dist_diff / time_diff
            if speed > max_speed:
                max_speed = speed

    print(max_speed)

if __name__ == '__main__':
    main()
