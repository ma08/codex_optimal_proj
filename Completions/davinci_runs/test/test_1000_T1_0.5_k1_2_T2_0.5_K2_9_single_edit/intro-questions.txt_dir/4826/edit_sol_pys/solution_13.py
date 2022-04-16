

import sys

def main():
    n = int(sys.stdin.readline().strip()) # number of elements
    k = int(sys.stdin.readline().strip()) # number of operations
    a = [int(x) for x in sys.stdin.readline().split()] # list of elements

    for i in range(k):
        b, c = [int(x) for x in sys.stdin.readline().split()]

        # update the number of elements
        n = n + (c - b)

        # update the list of elements
        a = a[:b-1] + [c] * (c-b) + a[c:]

        # print the max of the list
        print(max(a))

if __name__ == '__main__':
    main()
