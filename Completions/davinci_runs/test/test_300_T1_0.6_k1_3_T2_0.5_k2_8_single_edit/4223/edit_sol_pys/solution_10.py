


def slime_count(input_string):
    """
    >>> slime_count('aabbbbaacaa')
    5
    >>> slime_count('aabbbaaacaa')
    5
    >>> slime_count('aabbbaaccca')
    4
    >>> slime_count('aabbbaaaccca')
    4
    """
    counter = 1
    for i in range(1, len(input_string)):
        if input_string[i] != input_string[i - 1]:
            counter += 1
    return counter


if __name__ == "__main__":
    input_string = input()
    print(slime_count(input_string))
