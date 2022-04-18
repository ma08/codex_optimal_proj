

def main():
    # Read input
    n = int(input())
    intervals = [[]] * n
    for i in range(n):
        intervals[i] = [int(i) for i in input().split(" ")]

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
