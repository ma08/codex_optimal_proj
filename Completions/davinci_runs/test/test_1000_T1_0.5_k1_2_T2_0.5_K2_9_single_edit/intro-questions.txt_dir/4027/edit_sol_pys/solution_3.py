
# Solution:

import sys

def is_even(x):
    return x % 2 == 0

def is_odd(x):
    return not is_even(x)

def main():
    num = int(sys.stdin.readline())
    print(is_even(num))

if __name__ == '__main__':
    main()
