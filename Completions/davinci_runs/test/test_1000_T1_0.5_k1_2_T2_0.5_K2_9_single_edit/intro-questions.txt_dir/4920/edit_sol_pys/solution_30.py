
import sys

def main(input_str):
    """
    >>> main("abbcccddddeeeee")
    10
    """
    count = 1
    last = input_str[0]
    for c in input_str[1:]:
        if c != last:
            count += 1
        last = c
    return count - 1

if __name__ == '__main__':
    input_str = sys.stdin.readline().strip()
    print(main(input_str))
