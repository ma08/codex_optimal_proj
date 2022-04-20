

def find_max_removal(s, n):
    """
    Counts the maximum number of adjacent red and blue cubes that can be removed
    :param s: string of 1s and 0s (length n)
    :param n: length of string
    :return: maximum number of adjacent red and blue cubes that can be removed
    """
    # Initialize variables
    max_removal = 0
    prev_digit = None
    counter = 0
    for i in range(n):
        # If the digit is the same as the previous digit, increment the counter
        if s[i] == prev_digit:
            counter += 1
        # If the digit is different from the previous digit, update max_removal
        else:
            max_removal = max(max_removal, counter)
            counter = 1
        prev_digit = s[i]
    # Update max_removal one last time after the loop
    max_removal = max(max_removal, counter)
    return max_removal


if __name__ == "__main__":
    s = input()
    n = len(s)
    max_removal = find_max_removal(s, n)
    print(max_removal)
