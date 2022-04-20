

import sys

def main():
    # get input
    n = int(sys.stdin.readline())
    v = [int(x) for x in sys.stdin.readline().split()]
    v.sort()
    # start with the two smallest values
    total = (v[0] + v[1]) / 2
    # iterate through the rest of the values
    for i in range(2, n):
        # find the new total
        total = (total + v[i]) / 2
    # print the result
    print(total)

if __name__ == "__main__":
    main()