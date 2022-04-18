#!/usr/bin/python3

import sys

def main():
    n = int(sys.stdin.readline().strip())
    max_speed = 0
    prev_time = 0
    prev_dist = 0
    for i in range(n):
        time, dist = map(int, sys.stdin.readline().strip().split())
        speed = (dist - prev_dist) / (time - prev_time)
        if speed > max_speed:
            max_speed = speed
        prev_time, prev_dist = time, dist
    print(int(max_speed)) # print the result
    
if __name__ == "__main__":
    main()
