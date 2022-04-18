

def main():
    # Read input and split into list of integers
    input_list = [int(i) for i in input().split(" ")]
    # Get number of intervals
    n = input_list[0]
    # Get starting and ending points
    intervals = [input_list[i:i + 2] for i in range(1, len(input_list), 2)]

    # Check for common time by iterating over all intervals
    times = []

    # Check if all times are the same
    for interval in intervals:
        for time in range(interval[0], interval[1] + 1):
            times.append(time)
    if len(set(times)) == 1:
        print("Gunilla has a point")
    else:
        print("Edward is right")

if __name__ == "__main__":
    main()
