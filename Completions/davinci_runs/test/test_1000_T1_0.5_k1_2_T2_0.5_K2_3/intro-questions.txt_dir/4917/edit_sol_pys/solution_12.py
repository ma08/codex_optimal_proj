
import sys

def solve(times):
    # if any time is within another time, it is impossible
    # otherwise, possible 
    for time in times:
        for other_time in times:
            if time != other_time and time[0] >= other_time[0] and time[1] <= other_time[1]:
                return "Gunilla has a point"
    return "Edward is right"

def main():
    n = int(sys.stdin.readline().strip())
    times = []
    for _ in range(n):
        times.append(tuple(map(int, sys.stdin.readline().strip().split())))
    print(solve(times))

if __name__ == "__main__":
    main()
