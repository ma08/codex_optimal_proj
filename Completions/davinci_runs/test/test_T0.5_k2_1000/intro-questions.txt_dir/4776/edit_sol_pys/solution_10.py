#!/usr/bin/env python3

import sys

def main():
    events = int(sys.stdin.readline().strip())
    days = []
    for i in range(events):
        days.append(list(map(int, sys.stdin.readline().strip().split())))
    days.sort()
    intervals = []
    for day in days:
        if len(intervals) == 0:
            intervals.append(day)
        else:
            if intervals[-1][1] >= day[0]:
                intervals[-1][1] = max(intervals[-1][1], day[1])
            else:
                intervals.append(day)
    days_served = 0
    for start, end in intervals:
        days_served += end - start + 1
    print(days_served)

if __name__ == "__main__":
    main()
