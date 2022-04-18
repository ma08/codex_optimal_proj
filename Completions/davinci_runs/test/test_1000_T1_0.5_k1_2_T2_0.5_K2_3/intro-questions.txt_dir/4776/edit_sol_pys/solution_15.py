

import sys

def main():
    events = int(sys.stdin.readline().strip())
    days = []
    for i in range(events):
        days.append(list(map(int, sys.stdin.readline().strip().split())))
    days.sort()
    intervals = [] # list of intervals
    for start, end in days:
        if len(intervals) == 0:
            intervals.append([start, end])
        else:
            if intervals[-1][1] >= start: # if the interval overlaps with the previous interval
                intervals[-1][1] = max(intervals[-1][1], end) # extend the previous interval
            else:
                intervals.append([start, end]) # add a new interval
    days_served = 0
    for start, end in intervals:
        days_served += end - start + 1
    print(days_served)

if __name__ == "__main__":
    main()
