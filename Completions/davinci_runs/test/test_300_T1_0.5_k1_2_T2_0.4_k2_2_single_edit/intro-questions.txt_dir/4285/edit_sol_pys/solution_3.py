#!/usr/bin/env python3

import sys

def main():
    # read number of lines
    n = int(sys.stdin.readline().strip())

    # read lines
    lines = []
    for _ in range(n):
        lines.append(sys.stdin.readline().strip())

    # count number of lines
    count = 0

    for line in lines:
        # count number of a, b, c, ?
        na = line.count('a')
        nb = line.count('b')
        nc = line.count('c')
        nq = line.count('?')

        # if there are no ? in line, check if there is a subsequence abc
        if nq == 0:
            if 'abc' in line:
                count += 1
            continue

        # if there are no a, b, c in line, count number of subsequences abc
        if na == 0 and nb == 0 and nc == 0:
            count += 3 ** nq
            continue

        # prepare a list of possible positions of ?
        qs = [i for i in range(len(line)) if line[i] == '?']

        # count number of subsequences abc
        for i in range(3 ** nq):
            # replace ? with a, b, c
            t = line
            for j, q in enumerate(qs):
                t = t[:q] + 'abc'[i // (3 ** (nq - j - 1)) % 3] + t[q + 1:]

            # count number of subsequences abc
            if 'abc' in t:
                count += 1

    # print result
    print(count)

if __name__ == '__main__':
    main()
