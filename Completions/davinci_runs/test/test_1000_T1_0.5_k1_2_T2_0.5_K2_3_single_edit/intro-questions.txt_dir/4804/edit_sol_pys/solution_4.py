
# Solution:

import sys


def main():
    s = int(input())
    print(s, ":")
    for x in range(2, s+1):
        for y in range(1, x):
            if 2*y+x <= s and s % (x+y) == 0:
                print(x, ",", y)


main()
