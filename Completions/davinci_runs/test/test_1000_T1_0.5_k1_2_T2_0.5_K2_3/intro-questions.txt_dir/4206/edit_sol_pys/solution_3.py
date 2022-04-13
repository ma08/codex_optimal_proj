

# https://open.kattis.com/problems/filip

import sys

def main():
    # read the input and convert it to a list of integers
    a, b = sys.stdin.readline().split()
    a = list(map(int, a))
    b = list(map(int, b))

    # reverse the lists
    a.reverse()
    b.reverse()

    # compare the lists
    for i in range(3):
        if a[i] > b[i]:
            print(a[0], a[1], a[2], sep='')
            return 0
        elif a[i] < b[i]:
            print(b[0], b[1], b[2], sep='')
            return 0

    # if the lists are equal, print the first one
    print(a[0], a[1], a[2], sep='')

    return 0

if __name__ == "__main__":
    main()
