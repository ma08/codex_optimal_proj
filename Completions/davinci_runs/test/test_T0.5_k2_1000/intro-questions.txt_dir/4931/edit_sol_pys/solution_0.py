import sys
import math

def main():
    x, y = [int(i) for i in input().split()]
    if y == 0:
        print("IMPOSSIBLE")
        return
    if x == 0:
        print("ALL GOOD")
        return
    print(x / y)

if __name__ == '__main__':
    main()
