

def find_max_removal(s):
    """
    Finds the maximum number of adjacent red and blue cubes that can be removed
    :param s: string of 1s and 0s (1 = red, 0 = blue)
    :return: maximum number of adjacent red and blue cubes that can be removed (int)
    """
    # Initialize variables (max_removal = max number of cubes that can be removed, prev_digit = previous digit,
    # counter = number of adjacent cubes of the same color)
    max_removal = 0
    prev_digit = None
    counter = 0
    for digit in s:
        # If the digit is the same as the previous digit, increment the counter
        if digit == prev_digit:
            counter += 1
        # If the digit is different from the previous digit, update max_removal and reset the counter
        else:
            max_removal = max(max_removal, counter)
            counter = 1
        prev_digit = digit
    # Update max_removal one last time after the loop to account for the last set of adjacent cubes
    max_removal = max(max_removal, counter)
    return max_removal


if __name__ == "__main__":
    s = input()
    max_removal = find_max_removal(s)
    print(max_removal)
