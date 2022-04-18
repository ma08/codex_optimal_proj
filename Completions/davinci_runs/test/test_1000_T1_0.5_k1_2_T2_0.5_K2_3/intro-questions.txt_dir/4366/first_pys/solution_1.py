

import sys

def main():
    line = sys.stdin.readline()
    A,B = line.split()
    A = int(A)
    B = int(B)
    print((A+B)%24)

if __name__ == '__main__':
    main()