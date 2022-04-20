

import sys

def main():
    x = float(sys.stdin.readline())
    a = int(round(x, 0)) # round to the nearest integer
    b = int(round(x * 10, 0)) - a * 10 # round to the nearest integer and remove the integer part
    print(a, b)

if __name__ == '__main__':
    main()
