def slime_count(input_string):
    """
    >>> slime_count('aabbbbaacc')
    5
    >>> slime_count('aabbbaaacc')
    5
    >>> slime_count('aabbbaaacccc')
    4
    >>> slime_count('aabbbaaaccc')
    4
    """
    counter = 0
    for i in range(len(input_string) - 1):
        if input_string[i] == input_string[i + 1]:
            counter += 1
    return counter + 1


if __name__ == "__main__":
    input_string = input()
    print(slime_count(input_string))
