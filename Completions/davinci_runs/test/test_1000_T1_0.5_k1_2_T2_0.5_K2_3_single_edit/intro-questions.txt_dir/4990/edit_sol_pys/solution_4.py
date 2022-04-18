

import sys

def main(args):
    b, k, g = [int(x) for x in args[2].split()]
    days = 0
    while b > 0:
        days += 1
        b -= g
        if b < 0:
            break
        b -= k-g
    print(days)

if __name__ == '__main__':
    main(sys.argv)
