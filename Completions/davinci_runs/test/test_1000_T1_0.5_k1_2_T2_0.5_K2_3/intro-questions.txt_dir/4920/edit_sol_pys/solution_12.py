
import sys

def main(input):
    """
    >>> main("abbcccddddeeeee")
    a1b2c3d4e5
    """
    result = []
    count = 0
    for c in input:
        if len(result) == 0 or c == result[-1]:
            count += 1
        else:
            result.append(str(count))
            result.append(c)
            count = 1
    result.append(str(count))
    return ''.join(result)

if __name__ == '__main__':
    input = sys.stdin.readline().strip()
    print(main(input))
