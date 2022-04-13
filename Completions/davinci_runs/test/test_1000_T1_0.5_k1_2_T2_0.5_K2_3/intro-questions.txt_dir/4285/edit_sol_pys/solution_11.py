

import sys, math

def main():
    # read number of test cases
    t = int(sys.stdin.readline())

    for i in range(t):
        # read n, k
        n, k = map(int, sys.stdin.readline().split())

        # read a
        a = list(map(int, sys.stdin.readline().split()))

        # calculate sum of a
        sa = sum(a)

        # calculate minimum sum of a
        smin = min(a)

        # calculate maximum sum of a
        smax = max(a)

        # calculate minimum possible sum
        s0 = sa + k * smin

        # calculate maximum possible sum
        s1 = sa + k * smax

        # calculate minimum possible sum for each element
        s0s = [s0 - (k - 1) * x for x in a]

        # calculate maximum possible sum for each element
        s1s = [s1 - (k - 1) * x for x in a]

        # print result
        print(' '.join(map(str, s0s)))
        print(' '.join(map(str, s1s)))

if __name__ == '__main__':
    main()
