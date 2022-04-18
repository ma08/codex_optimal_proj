

def main():
    # Read input
    n = int(raw_input())
    intervals = []
    for i in range(n):
        intervals.append([int(i) for i in raw_input().split(" ")])

    # Check for common time interval
    times = []
    for interval in intervals:
        for time in range(interval[0], interval[1] + 1):
            times.append(time)
    if len(set(times)) == 1:
        print("gunilla has a point")
    else:
        print("edward is right")

if __name__ == "__main__":
    main()
