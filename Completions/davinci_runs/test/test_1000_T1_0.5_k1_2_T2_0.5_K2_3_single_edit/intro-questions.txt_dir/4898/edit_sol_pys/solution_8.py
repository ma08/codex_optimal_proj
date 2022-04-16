
import sys

def main(pname):
    # sys.stdin = open(pname + '.in', 'r')
    # sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    intervals = []
    for i in range(n):
        l, u = [int(j) for j in input().split()]
        intervals.append((l, u))
    intervals.sort()
    room_count = 0
    curr_room = intervals[0][0]
    for i in range(n):
        if intervals[i][0] <= curr_room:
            curr_room = max(curr_room, intervals[i][1])
        else:
            room_count += 1
            curr_room = intervals[i][1]
    print(room_count + 1)

if __name__ == "__main__":
    main('airconditioned')
