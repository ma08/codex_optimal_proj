import sys


def main(input_):
    """
    >>> main("abbcccddddeeeee") # doctest: +NORMALIZE_WHITESPACE
    10
    """
    count = 1
    last = input_[0]
    for c in input_[1:]:
        if c != last:
            count += 1
        last = c
    return count - 1


if __name__ == '__main__':
    input = sys.stdin.readline().strip()
    print(main(input))
