

import sys

    """
    >>> is_harshad(10)
    True
    >>> is_harshad(12)
    False
    >>> is_harshad(18)
    True
    >>> is_harshad(11)
    False
    >>> is_harshad(13)
    False
    """
def is_harshad(n):
    n = str(n)
    return int(n) % sum([int(i) for i in n]) == 0

    """
    >>> next_harshad(10)
    12
    >>> next_harshad(18)
    20
    >>> next_harshad(19)
    20
    >>> next_harshad(21)
    24
    >>> next_harshad(1000)
    1002
    """
def next_harshad(n):
    n += 1
    while not is_harshad(n):
        n += 1
    return n

def main():
    n = int(sys.stdin.readline())
    print(next_harshad(n))

if __name__ == "__main__":
    main()
