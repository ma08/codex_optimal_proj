
def slime_count(input_string):
    """
    >>> slime_count("aabbbbaaca")
    4
    >>> slime_count("aabbbaaaca")
    4
    >>> slime_count("aabbbaaccc")
    3
    >>> slime_count("aabbbaaaccc")
    3
    """
    counter = 1
    for i in range(1, len(input_string)):
        if input_string[i] != input_string[i - 1]:
            counter += 1
    return counter


if __name__ == "__main__":
    input_string = input()
    print(slime_count(input_string))
