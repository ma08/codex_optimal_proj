"""
This is a file
"""

import sys

    """
    This is a main function
    """
def main():
    a, b, c = map(int, sys.stdin.readline().split(' '))
    if a + b == c:
        print(a + b)
    elif a + c == b:
        print(a + c)
    elif b + c == a:
        print(b + c)

if __name__ == '__main__':
    main()
