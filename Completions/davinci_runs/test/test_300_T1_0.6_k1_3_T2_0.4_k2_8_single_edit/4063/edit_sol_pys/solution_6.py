


def main():
    # Read the number of students
    N = int(input())  # type: int

    # Read the height of each student
    heights = [int(x) for x in input().split()]  # type: list[int]

    # Sort the heights in ascending order
    heights.sort()

    # Calculate the number of students for each height
    heights_by_count = {}
    for height in heights:
        if height not in heights_by_count:
            heights_by_count[height] = 0
        heights_by_count[height] += 1

    # Calculate the number of choices of the integer X
    count = 0
    for height in heights_by_count:
        if height in heights_by_count:
            count += heights_by_count[height] * heights_by_count[N//2-height]

    # Print the answer
    print(count)


if __name__ == '__main__':
    main()
