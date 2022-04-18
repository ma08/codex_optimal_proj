

import sys

def main():
    n = int(sys.stdin.readline().rstrip('\n'))
    intervals = []
    for i in range(n):
        a, b = [int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        intervals.append([a, b])
    intervals.sort()
    intervals_in_common = []
    for i in range(n):
        for j in range(n):
            if i != j:
                start = max(intervals[i][0], intervals[j][0])
                end = min(intervals[i][1], intervals[j][1])
                if start <= end:
                    intervals_in_common.append([start, end])
    print(intervals_in_common)

if __name__ == '__main__':
    main()
