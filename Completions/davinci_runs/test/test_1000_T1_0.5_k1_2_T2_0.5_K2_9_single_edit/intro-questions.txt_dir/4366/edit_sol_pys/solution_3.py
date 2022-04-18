import math

import sys

def main():
    line = sys.stdin.readlines()
    for i in line:
        A,B = i.split()
        A = int(A)
        B = int(B)
        print((A+B)%24)

if __name__ == '__main__':
    main()
