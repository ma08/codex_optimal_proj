

import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    # count number of unique values
    unique_values = len(set(a))

    # print number of pockets needed
    print(unique_values)

if __name__ == '__main__':
    main()