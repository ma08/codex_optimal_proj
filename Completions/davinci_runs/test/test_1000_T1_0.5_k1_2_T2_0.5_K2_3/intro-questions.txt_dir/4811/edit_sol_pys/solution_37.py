

def count_substrings(haystack, needle):
    count = 0
    for i in range(len(haystack)):
        if haystack[i: i + len(needle)] == needle:
            count += 1
    return count

def contains(big_string, little_string):
    return little_string in big_string


def common_letters(string_one, string_two):
    common = []
    for letter in string_one:
        if (letter in string_two) and not (letter in common):
            common.append(letter)
    return common


def main():
    """Read and print an integer series."""

    # Read an initial series from standard input
    data = input('Enter some integers: ')
    numbers = data.split()
    print(numbers)
    print(len(numbers))
    print(numbers[0])
    print(numbers[1])
    print(numbers[2])
    print(numbers[-1])
    print(numbers[-2])
    print(numbers[-3])

    # Convert the strings to ints
    numbers = [int(x) for x in numbers]
    print(numbers)

    # Print the series
    print('The series:')
    for number in numbers:
        print(number)

    # Print the length of the series
    print('The length of the series is', len(numbers))

    # Print the smallest and largest numbers in the series
    print('The smallest number is', min(numbers))
    print('The largest number is', max(numbers))

    # Print the sum of the series
    print('The sum of the series is', sum(numbers))

    # Print the average of the series
    print('The average of the series is', sum(numbers) / len(numbers))


if __name__ == '__main__':
    main()
