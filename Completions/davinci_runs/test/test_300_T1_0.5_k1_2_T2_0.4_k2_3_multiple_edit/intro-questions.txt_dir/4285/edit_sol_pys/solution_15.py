
import sys

def main():
    # read number of chars
    n = int(sys.stdin.readline())
    # read characters
    s = sys.stdin.readline().strip()

    # count number of 'a', 'b', 'c', '?'
    na = s.count('a')
    nb = s.count('b')
    nc = s.count('c')
    nq = s.count('?')

    # if there are no ? in s, check if there is a subsequence abc
    if nq == 0:
        if 'abc' in s:
            print(1)
        else:
            print(0)
        return

    # if there are no a, b, c in s, count number of subsequences abc
    if na == 0 and nb == 0 and nc == 0:
        print(3 ** nq)
        return

    # prepare a list of possible positions of ?
    qs = [i for i in range(n) if s[i] == '?']

    # count number of subsequences abc in s
    count = 0

    for i in range(3 ** nq):
        # replace ? with a, b, c
        t = s
        for j, q in enumerate(qs):
            t = t[:q] + 'abc'[i // (3 ** (nq - j - 1)) % 3] + t[q + 1:]

        # count number of subsequences abc in s
        if 'abc' in t:
            count += 1

    # print result
    print(count)

if __name__ == '__main__':
    main()
