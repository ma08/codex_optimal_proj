
import sys

def main(input_string):
    """
    >>> main("abbcccddddeeeee")
    10
    """
    count = 1
    last = input_string[0]
    for c in input_string[1:]:
        if c != last:
            count += 1
        last = c
    return count - 1

if __name__ == '__main__':
    input_string = sys.stdin.readline().strip()
    print(main(input_string))
