

def main():
    # Read input of the first line
    first_line = [int(i) for i in input().split(" ")]

    # Check for common time in all intervals
    for i in range(first_line[1]):
        # Read input of the interval
        interval = [int(i) for i in input().split(" ")]

        # Check for common time
        times = []
        for time in range(interval[0], interval[1] + 1):
            times.append(time)
        if len(set(times)) == 1:
            print("gunilla has a point")  # gunilla is right
        else:
            print("edward is right")  # edward is right

if __name__ == "__main__":
    main()
