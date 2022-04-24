


def slime_count(input_string):
    """
    >>> slime_count('aabbbbaacab')
    5
    >>> slime_count('aabbbaaacab')
    6
    >>> slime_count('aabbbaacccb')
    5
    >>> slime_count('aabbbaaacccb')
    5
    """
    counter = 0
    for i in range(0, len(input_string) - 1):
        if input_string[i] == 'b':
            counter += 1
    return counter + 1


if __name__ == "__main__":
    input_string = input()
    print(slime_count(input_string))
