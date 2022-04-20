

def main():
    """
    This is the main function.
    """

    # Get the input
    n, m = map(int, input().split())
    segments = []
    for i in range(n):
        segments.append(tuple(map(int, input().split())))

    # Convert the segments to a set of numbers
    numbers = set()
    for segment in segments:
        for i in range(segment[0], segment[1] + 1):
            numbers.add(i)

    # Get the numbers that aren't in the set
    numbers = list(set(range(1, m + 1)) - numbers)
    numbers.sort()

    # Print the output
    print(len(numbers))
    print(" ".join(map(str, numbers)))

if __name__ == "__main__":
    main()