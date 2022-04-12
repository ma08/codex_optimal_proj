

def main():
    # Read input and store in a list
    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break

    # Check for common time
    for line in lines:
        times = []
        for interval in line:
            for time in range(interval[0], interval[1] + 1):
                times.append(time)
        if len(set(times)) == 1:
            print("gunilla has a point")  # Gunilla has a point
        else:
            print("edward is right")  # Edward is right

if __name__ == "__main__":
    main()
