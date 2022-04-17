

import sys, math

def main():
    # read number of chars
    n = int(input())
    # read chars
    s = input().strip()

    # count number of a, b, c, ?
    na, nb, nc, nq = s.count('a'), s.count('b'), s.count('c'), s.count('?')

    # if there are no ? in s, check if there is a subsequence abc
    if nq == 0:
        if 'abc' in s:
            print(1)
        else:
            print(0)
        return

    # prepare a list of possible positions of ?
    qs = [i for i in range(n) if s[i] == '?']

    # count number of subsequences abc with ? replaced by a, b, c
    count = 3 ** nq

    # count number of subsequences abc with ? replaced by a
    count -= 2 ** nq
    for i in range(nq):
        if s[qs[i] - 1] == 'a':
            count -= 2 ** (nq - i - 1)

    # count number of subsequences abc with ? replaced by b
    count -= 2 ** nq
    for i in range(nq):
        if s[qs[i] - 1] == 'b':
            count -= 2 ** (nq - i - 1)

    # count number of subsequences abc with ? replaced by c
    count -= 2 ** nq
    for i in range(nq):
        if s[qs[i] - 1] == 'c':
            count -= 2 ** (nq - i - 1)

    # print result
    print(count % (10 ** 9 + 7))

if __name__ == '__main__':
    main()
