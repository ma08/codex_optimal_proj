
import sys

def main(input):
    """
    >>> main("abbcccddddeeeee")
    10
    """
    count = 1
    last = input[0]
    for c in input[1:]:
        if c != last:
            count += 1
        last = c
    return count - 1

if __name__ == '__main__':
    #input = sys.stdin.readline().strip()
    #print(main(input))
    import doctest
    doctest.testmod()
