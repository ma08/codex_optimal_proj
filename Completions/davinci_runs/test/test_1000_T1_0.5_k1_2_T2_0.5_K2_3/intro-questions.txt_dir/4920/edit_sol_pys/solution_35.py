
import sys

def main(input):
    """
    >>> main("abbcccddddeeeeef")
    10
    >>> main("abbcccddddeeeeefffff")
    12
    >>> main("abbcccddddeeeeefffffa")
    13
    """
    count = 0
    last = input[0]
    for c in input[1:]:
        if c != last:
            count += 1
        last = c
    return count

if __name__ == '__main__':
    input = sys.stdin.readline().strip()
    print(main(input))
