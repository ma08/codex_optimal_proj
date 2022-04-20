

import sys

def main():
    args = sys.stdin.readline().split()
    A = int(args[0])
    B = int(args[1])

    print(B // A + B % A)

if __name__ == '__main__':
    main()