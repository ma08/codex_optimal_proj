
import sys

def main():
    events = int(sys.stdin.readline().strip())
    days = []
    for i in range(events):
        days.append(list(map(int, sys.stdin.readline().strip().split())))
    days.sort()
    intervals = []
    for start, end in days:
        if len(intervals) == 0:
            intervals.append([start, end])
        else:
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
