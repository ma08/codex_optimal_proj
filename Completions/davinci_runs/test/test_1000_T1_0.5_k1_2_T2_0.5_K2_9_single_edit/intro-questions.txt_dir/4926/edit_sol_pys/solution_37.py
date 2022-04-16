
# pylint: disable=C0103

import sys

def factorial(num):
    """Return the factorial of a number."""
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

def euler_approx(num):
    """Return the euler approximation of a number."""
    e = 0
    for i in range(num+1):
        e += 1/factorial(i)
    return e

def main():
    """Main function."""
    num = int(sys.stdin.readline())
    print(euler_approx(num))

if __name__ == '__main__':
    main()
