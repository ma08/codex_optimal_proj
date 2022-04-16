

import sys

def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    intervals = []
    for i in range(n):
        l, u = [int(j) for j in input().split()]
        intervals.append((l, u))
    intervals.sort()
    rooms = []
    rooms.append(intervals[0][1])
    for i in range(n):
        for j in range(len(rooms)):
            if intervals[i][0] >= rooms[j]:
                rooms[j] = intervals[i][1]
                break
        if j == len(rooms) - 1:
            rooms.append(intervals[i][1])
    print(len(rooms))

if __name__ == "__main__":
    main('airconditioned')
