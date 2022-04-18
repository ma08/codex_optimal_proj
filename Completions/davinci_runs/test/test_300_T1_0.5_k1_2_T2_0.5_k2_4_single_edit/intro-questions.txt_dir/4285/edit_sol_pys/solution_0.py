

import sys

def main():
    # read number of characters
    n = int(sys.stdin.readline())
    # read characters
    s = sys.stdin.readline().strip()

    # count the number of a, b, c, ?
    n_a = s.count('a')
    n_b = s.count('b')
    n_c = s.count('c')
    n_q = s.count('?')

    # if there are no ? in s, check if there is a subsequence "abc"
    if n_q == 0:
        if 'abc' in s:
            print(1)
        else:
            print(0)
        return

        return

    # if there are no a, b, c in s, count the number of subsequences "abc"
    if n_a == 0 and n_b == 0 and n_c == 0:
        print(3 ** n_q)
        return

        return

    # prepare a list of possible positions of ? in s
    qs = [i for i in range(n) if s[i] == '?']  # qs: question marks

    # count the number of subsequences "abc"
    count = 0

    for i in range(3 ** n_q):
        # replace ? with a, b, c in s
        t = s
        for j, q in enumerate(qs):
            t = t[:q] + 'abc'[i // (3 ** (n_q - j - 1)) % 3] + t[q + 1:]

        # count the number of subsequences "abc"
        if 'abc' in t:
            count += 1

    # print result
    print(count)

if __name__ == '__main__':
    main()
