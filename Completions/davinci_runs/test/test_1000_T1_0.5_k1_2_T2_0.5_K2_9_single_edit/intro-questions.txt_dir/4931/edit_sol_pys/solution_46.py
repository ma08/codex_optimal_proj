

import sys
import math

def main():
    x, y = [int(i) for i in sys.stdin.readline().split()] # get input
    if y == 1: # if y is 1, it's impossible
        print("IMPOSSIBLE")
        return
    if x == 0:
        print("ALL GOOD")
        return
    print(x / (y - 1))

if __name__ == '__main__':
    main()
