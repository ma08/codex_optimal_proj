


# Defining function for checking if a number is interesting
def is_interesting(n):
    """
    Returns true if number is interesting else returns false.
    """
    return int(sum(list(map(int, list(str(n))))) % 4) == 0


# Finding the nearest interesting number
def find_nearest_interesting_number(n):
    while not is_interesting(n):
        n += 1
    return n


if __name__ == '__main__':
    # Getting input
    n = int(input())

    # Printing the answer
    print(find_nearest_interesting_number(n))
