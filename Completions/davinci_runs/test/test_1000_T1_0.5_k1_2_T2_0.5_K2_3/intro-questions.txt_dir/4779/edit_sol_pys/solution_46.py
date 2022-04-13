

import sys

def main():
    input = sys.stdin.readline

    N = int(input().strip())
    A = list(map(int, [input().strip() for _ in range(N)]))
    A.sort()

    # (a1^2 + ... + ak^2) * (ak+1 + ... + an)
    # is maximized when ak+1 + ... + an is maximized
    # and a1^2 + ... + ak^2 is minimized
    # which is when a1 ... ak are the smallest numbers

    # (a1^2 + ... + ak^2) * (ak+1 + ... + an)
    # = (a1^2 + ... + ak^2) * (a1 + ... + an) - (a1^2 + ... + ak^2) * (a1 + ... + ak)
    # = (a1^2 + ... + ak^2) * (a1 + ... + an) - (a1^3 + ... + ak^3)
    # = (a1^2 + ... + ak^2) * (a1 + ... + an - a1 - ... - ak)
    # = (a1^2 + ... + ak^2) * (an - ak)
    # = (a1^2 + ... + ak^2) * (an - ak) * (an - ak)

    # a1^2 + ... + ak^2 is minimized when a1 ... ak are the smallest numbers
    # an - ak is maximized when an is the largest number and ak is the smallest number

    # so we can use the largest and smallest numbers
    # a1^2 + ... + ak^2 = a1^2 + ... + an^2 - (an+1^2 + ... + ak^2)

    # a1^2 + ... + ak^2 = a1^2 + ... + an^2 - (an+1^2 + ... + ak^2)
    # = a1^2 + ... + an^2 - (an+1^2 + ... + ak^2)
    # = a1^2 + ... + an^2 - (an+1^2 + ... + an^2)
    # = a1^2 + ... + an^2 - (an^2 + ... + an^2)
    # = a1^2 + ... + an^2 - (n - k) * an^2
    # = (k - (n - k)) * an^2

    # so the answer is (k - (n - k)) * an^2 * (an - a1)

    # we can use the largest and smallest numbers
    # (k - (n - k)) * an^2 * (an - a1)

    print((N - 1) * A[-1]**2 * (A[-1] - A[0]))

if __name__ == '__main__':
    main()
