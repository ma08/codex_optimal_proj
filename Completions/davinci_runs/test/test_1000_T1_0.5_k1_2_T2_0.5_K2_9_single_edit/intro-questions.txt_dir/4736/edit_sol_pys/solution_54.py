
import math
import operator as op

from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, range(n, n-r, -1))
    denom = reduce(op.mul, range(1, r+1))

    return numer//denom

def main():
    card_counts = list(map(int, input().strip().split()))
    k = int(input().strip())

    # If there are not enough cards to deal, return 0
    if sum(card_counts) < k:
        print(0)
        return

    # If there are exactly k cards to deal, return 1
    if sum(card_counts) == k:
        print(1)
        return

    # If there are more cards to deal than numbers, return 0
    if k > 10:
        print(0)
        return


    # Find the number of combinations
    combinations = 0
    for i in range(k):
        combinations += ncr(sum(card_counts[i:]), k-i)

    print(combinations)

if __name__ == '__main__':
    main()
