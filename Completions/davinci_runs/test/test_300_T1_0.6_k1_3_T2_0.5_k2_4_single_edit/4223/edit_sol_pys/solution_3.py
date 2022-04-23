
def slime_count(input_string):
    """
    >>> slime_count('aabbbbaaca')
    5
    >>> slime_count('aabbbaaaca')
    5
    >>> slime_count('aabbbaaccc')
    4
    >>> slime_count('aabbbaaaccc')
    >>> slime_count('aabbbaaaccccc')
    4
    4
    """
    if len(input_string) == 0:
        return 0
    elif len(input_string) == 1:
        return 1
    elif len(input_string) == 2:
        if input_string[0] == input_string[1]:
            return 1
        else:
            return 2
    else:
        if input_string[0] == input_string[1]:
            return slime_count(input_string[1:])
        else:
            return 1 + slime_count(input_string[1:])


if __name__ == "__main__":
    input_string = input()
    print(slime_count(input_string))
