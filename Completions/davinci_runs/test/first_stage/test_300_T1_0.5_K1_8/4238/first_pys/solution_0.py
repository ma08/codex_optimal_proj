

import sys


def is_multiple_of_9(n: int) -> bool:
    if n % 9 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    if is_multiple_of_9(n):
        print('Yes')
    else:
        print('No')