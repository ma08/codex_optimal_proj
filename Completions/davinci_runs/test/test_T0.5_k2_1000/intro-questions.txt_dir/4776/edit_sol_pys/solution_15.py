#!/usr/bin/env python3

import sys

def main():
    events = int(sys.stdin.readline().strip())
    days = [list(map(int, sys.stdin.readline().strip().split())) for i in range(events)]
    days.sort()
    intervals = [days[0]]
    for start, end in days[1:]:
        if intervals[-1][1] >= start:
            intervals[-1][1] = max(intervals[-1][1], end)
        else:
            intervals.append([start, end])
    days_served = 0
    for start, end in intervals:
        days_served += end - start + 1
    print(days_served)

if __name__ == "__main__":
    main()
