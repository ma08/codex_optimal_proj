
import sys

def get_missing_numbers(n, recited):
    """
    Find missing numbers.

    :param n: number of numbers that should be recited
    :param recited: list of numbers recited by the student
    :return: list of missing numbers
    """
    missing = []
    for i in range(1, recited[-1] + 1):
        if i not in recited:
            missing.append(i)

    return missing


def main():
    # Read lines from stdin
    lines = [line.strip() for line in sys.stdin]

    # Parse input
    n = int(lines[0])
    recited = [int(line) for line in lines[1:]]

    # Find missing numbers
    missing = get_missing_numbers(n, recited)

    # Print results
    if len(missing) == 0:
        print("good job")
    else:
        for num in missing:
            print(num)


if __name__ == "__main__":
    main()
