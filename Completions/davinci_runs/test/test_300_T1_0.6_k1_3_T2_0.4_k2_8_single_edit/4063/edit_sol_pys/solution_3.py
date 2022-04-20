


def main():
    # Read the number of elements
    N = int(input().strip())

    # Read the elements
    elements = [int(x) for x in input().split()]

    # Sort the elements in ascending order
    elements.sort()

    # Calculate the number of elements for each difficulty
    elements_by_difficulty = {}
    for element in elements:
        if element not in elements_by_difficulty:
            elements_by_difficulty[element] = 0
        elements_by_difficulty[element] += 1

    # Calculate the number of choices of the integer K
    count = 0
    for difficulty in elements_by_difficulty:
        if difficulty in elements_by_difficulty:
            count += elements_by_difficulty[difficulty] * elements_by_difficulty[N//2-difficulty]

    # Print the answer
    print(count)


if __name__ == '__main__':
    main()
