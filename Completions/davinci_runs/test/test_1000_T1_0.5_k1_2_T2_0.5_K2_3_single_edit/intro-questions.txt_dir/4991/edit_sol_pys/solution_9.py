

# The answer is:

import sys

    """
    This function will return the sum of the hailstone sequence for the given n.
    """
def hailstone(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + hailstone(n//2)
    else:
        return n + hailstone((3*n)+1)

    """
    This is the main function.
    """
def main():
    n = int(sys.stdin.readline())
    print(hailstone(n))

if __name__ == '__main__':
    main()
