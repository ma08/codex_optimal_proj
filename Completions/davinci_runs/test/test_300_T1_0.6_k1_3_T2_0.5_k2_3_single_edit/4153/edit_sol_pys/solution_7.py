

def find_max_removal(s):
    """
    Counts the maximum number of adjacent red and blue cubes that can be removed
    :param s: string of 1s and 0s to represent the cubes
    :return: maximum number of adjacent red and blue cubes that can be removed
    """
    # Initialize variables
    max_removal = 0
    prev_digit = None
    counter = 0
    for digit in s:
        # If the digit is the same as the previous digit, increment the counter
        if digit == prev_digit:
            counter += 1
        # If the digit is different from the previous digit, update max_removal
        else:
            max_removal = max(max_removal, counter)
            counter = 1
        prev_digit = digit
    # Update max_removal one last time after the loop
    max_removal = max(max_removal, counter)
    return max_removal


if __name__ == "__main__":
    s = input()
    max_removal = find_max_removal(s)
    print(max_removal)
