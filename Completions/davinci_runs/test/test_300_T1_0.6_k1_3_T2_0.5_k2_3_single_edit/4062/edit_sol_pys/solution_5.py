"""
https://www.hackerrank.com/challenges/rectangle-area/problem
"""

import sys

def main():
    a, b, c, d = [int(x) for x in sys.stdin.readline().split()]
    x = min(a, c)
    y = max(b, d)
    print(x * y)

if __name__ == '__main__':
    main()
