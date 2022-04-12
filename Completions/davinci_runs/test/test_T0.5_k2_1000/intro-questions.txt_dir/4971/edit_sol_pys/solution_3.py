

import sys

def main():
    m = int(sys.stdin.readline().strip()) # read the input
    x = 1
    while x <= m: # loop through all possible values of x
        if len(set([a**3 + b**3 for a in range(1, x) for b in range(1, x)])) == x:
            return x # return the first value of x that satisfies the condition
        x += 1
    return 'none' # return none if no value of x satisfies the condition

print(main())
