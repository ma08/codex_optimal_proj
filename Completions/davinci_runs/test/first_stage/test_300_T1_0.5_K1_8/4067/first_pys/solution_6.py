

import sys

def minimum_replacement(n, s):
    """
    >>> minimum_replacement(3, '121')
    '021'
    >>> minimum_replacement(6, '000000')
    '001122'
    >>> minimum_replacement(6, '211200')
    '211200'
    >>> minimum_replacement(6, '120110')
    '120120'
    """
    n_zeros = 0
    n_ones = 0
    n_twos = 0
    for i in s:
        if i == '0':
            n_zeros += 1
        elif i == '1':
            n_ones += 1
        elif i == '2':
            n_twos += 1
    if n_zeros > n_ones:
        for i in range(n_zeros - n_ones):
            s = s.replace('0', '1', 1)
    elif n_zeros < n_ones:
        for i in range(n_ones - n_zeros):
            s = s.replace('1', '0', 1)
    if n_ones > n_twos:
        for i in range(n_ones - n_twos):
            s = s.replace('1', '2', 1)
    elif n_ones < n_twos:
        for i in range(n_twos - n_ones):
            s = s.replace('2', '1', 1)
    return s

if __name__ == "__main__":
    n = int(input())
    s = input()
    print(minimum_replacement(n, s))