

def simplify(s):
    """Simplify a string of lowercase letters.

    >>> simplify('aabbcc')
    3
    >>> simplify('aabbccc')
    3
    >>> simplify('aabbcccc')
    3
    >>> simplify('aabbccccc')
    4
    >>> simplify('aabbcccccc')
    4
    >>> simplify('aabbccccccc')
    5
    >>> simplify('aabbcccccccc')
    5
    >>> simplify('aabbccccccccc')
    6
    >>> simplify('aabbcccccccccc')
    6
    >>> simplify('aabbccccccccccc')
    7
    >>> simplify('aabbcccccccccccc')
    7
    >>> simplify('aabbccccccccccccc')
    8
    >>> simplify('aabbcccccccccccccc')
    8
    >>> simplify('aabbccccccccccccccc')
    9
    >>> simplify('aabbcccccccccccccccc')
    9
    >>> simplify('aabbccccccccccccccccc')
    10
    >>> simplify('aabbcccccccccccccccccc')
    10
    >>> simplify('aabbccccccccccccccccccc')
    11
    >>> simplify('aabbcccccccccccccccccccc')
    11
    >>> simplify('aabbccccccccccccccccccccc')
    12
    >>> simplify('aabbcccccccccccccccccccccc')
    12
    >>> simplify('aabbccccccccccccccccccccccc')
    13
    >>> simplify('aabbcccccccccccccccccccccccc')
    13
    >>> simplify('aabbccccccccccccccccccccccccc')
    14
    >>> simplify('aabbcccccccccccccccccccccccccc')
    14
    >>> simplify('aabbccccccccccccccccccccccccccc')
    15
    >>> simplify('aabbcccccccccccccccccccccccccccc')
    15
    >>> simplify('aabbccccccccccccccccccccccccccccc')
    16
    >>> simplify('aabbcccccccccccccccccccccccccccccc')
    16
    >>> simplify('aabbccccccccccccccccccccccccccccccc')
    17
    >>> simplify('aabbcccccccccccccccccccccccccccccccc')
    17
    >>> simplify('aabbccccccccccccccccccccccccccccccccc')
    18
    >>> simplify('aabbcccccccccccccccccccccccccccccccccc')
    18
    >>> simplify('aabbccccccccccccccccccccccccccccccccccc')
    19
    >>> simplify('aabbcccccccccccccccccccccccccccccccccccc')
    19
    >>> simplify('aabbccccccccccccccccccccccccccccccccccccc')
    20
    >>> simplify('aabbcccccccccccccccccccccccccccccccccccccc')
    20
    >>> simplify('aabbccccccccccccccccccccccccccccccccccccccc')
    21
    >>> simplify('aabbcccccccccccccccccccccccccccccccccccccccc')
    21
    >>> simplify('aabbccccccccccccccccccccccccccccccccccccccccc')
    22
    >>> simplify('aabbcccccccccccccccccccccccccccccccccccccccccc')
    22
    >>> simplify('aabbccccccccccccccccccccccccccccccccccccccccccc')
    23
    >>> simplify('aabbcccccccccccccccccccccccccccccccccccccccccccc')
    23
    >>> simplify('aabbccccccccccccccccccccccccccccccccccccccccccccc')
    24
    >>> simplify('aabbcccccccccccccccccccccccccccccccccccccccccccccc')
    24
    >>> simplify('aabbccccccccccccccccccccccccccccccccccccccccccccccc')
    25
    >>> simplify('aabbcccccccccccccccccccccccccccccccccccccccccccccccc')
    25
    >>> simplify('aabbccccccccccccccccccccccccccccccccccccccccccccccccc')
    26
    >>> simplify('aabbcccccccccccccccccccccccccccccccccccccccccccccccccc')
    26
    >>> simplify('aabbccccccccccccccccccccccccccccccccccccccccccccccccccc')
    27
    >>> simplify('aabbcccccccccccccccccccccccccccccccccccccccccccccccccccc')
    27
    >>> simplify('aabbccccccccccccccccccccccccccccccccccccccccccccccccccccc')
    28
    >>> simplify('aabbcccccccccccccccccccccccccccccccccccccccccccccccccccccc')
    28
    >>> simplify('aabbccccccccccccccccccccccccccccccccccccccccccccccccccccccc')
    29
    >>> simplify('aabbcccccccccccccccccccccccccccccccccccccccccccccccccccccccc')
    29
    >>> simplify('aabbccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')
    30
    >>> simplify('aabbcccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')
    30
    >>> simplify('aabbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')
    31
    >>> simplify('aabbcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')
    31
    >>> simplify('aabbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')
    32
    >>> simplify('aabbcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')
    32
    >>> simplify('aabbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')
    33
    >>> simplify('aabbcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')
    33
    """
    return len(set(s))

def erase(s):
    """Find minimum number of letters to erase to simplify a string.

    >>> erase('aabbcc')
    0
    >>> erase('aabbccc')
    0
    """
    if simplify(string) < 3:
        return 0
    for i in range(len(string)):
        if simplify(string[:i] + string[i + 1:]) < 3:
            return 1
    return 2

print(erase(input()))
