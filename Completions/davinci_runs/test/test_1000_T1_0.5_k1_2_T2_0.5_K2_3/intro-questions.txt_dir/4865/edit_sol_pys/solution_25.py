#!/usr/bin/env python3

import sys

def main():
    num_cases = int(sys.stdin.readline())
    for i in range(num_cases):
        line = sys.stdin.readline().split()
        direction = line[0]
        minutes = int(line[1])
        hours = int(line[2])
        min_of_day = int(line[3])
        if direction == "F":
            if min_of_day + minutes >= 60:
                hours = (hours + 1) % 24
                min_of_day = (min_of_day + minutes) % 60
            else:
                min_of_day += minutes
            print(hours, min_of_day)
        else:
            if min_of_day - minutes < 0:
                hours = hours - 1
                min_of_day = 60 + (min_of_day - minutes)
            else:
                min_of_day -= minutes
            print(hours, min_of_day)
main()
