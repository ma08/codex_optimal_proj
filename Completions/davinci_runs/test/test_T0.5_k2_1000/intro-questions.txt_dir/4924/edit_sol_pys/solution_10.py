#!/usr/bin/env python3

import sys
import datetime

def main():
    current_time = [int(x) for x in sys.stdin.readline().strip().split(':')]
    desired_time = [int(x) for x in sys.stdin.readline().strip().split(':')]
    current_time = datetime.datetime(2000, 1, 1, current_time[0], current_time[1], current_time[2])
    desired_time = datetime.datetime(2000, 1, 1, desired_time[0], desired_time[1], desired_time[2])
    if desired_time <= current_time:
        desired_time += datetime.timedelta(days=1)
    else:
        pass
    print((desired_time - current_time).total_seconds())

if __name__ == '__main__':
    main()
