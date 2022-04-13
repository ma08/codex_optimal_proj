"""
file
"""

import sys

def who_wins(n):
    if n % 2 == 1:
        return "Alice"
    else:
        return "Bob"

def main():
    n = int(sys.stdin.readline().strip()) # read int from stdin
    print(who_wins(n)) # print to stdout

if __name__ == '__main__':
    main()
