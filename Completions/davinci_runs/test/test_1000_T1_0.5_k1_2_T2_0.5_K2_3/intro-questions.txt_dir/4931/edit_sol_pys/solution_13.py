

import sys
import math

def main():
    x, y = [int(i) for i in sys.stdin.readline().split()]
    if y == 1:
        print("impossible")
        return
    if x == 0:
        print("all good!")
        return
    print(x / (y - 1))

if __name__ == '__main__':
    main()
