

def main():
    # Read input
    n = int(input())
    intervals = []
    for i in range(n):
        intervals.append(list(map(int, input().split())))

    # Check for common time
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
