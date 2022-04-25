# https://atcoder.jp/contests/abc119/tasks/abc119_d
# https://atcoder.jp/contests/abc119/submissions/4340376

import sys

def main():
    # read A, B, Q
    A, B, Q = [int(x) for x in sys.stdin.readline().split()]

    # read S
    S = [int(x) for x in sys.stdin.readline().split()]
    S.sort()
    S.insert(0, -10 ** 18 - 1)
    S.append(10 ** 18 + 1)

    # read T
    T = [int(x) for x in sys.stdin.readline().split()]
    T.sort()
    T.insert(0, -10 ** 18 - 1)
    T.append(10 ** 18 + 1)

    # read X
    X = [int(x) for x in sys.stdin.readline().split()]

    # calculate distances
    for x in X:
        # find closest points in S and T
        s = bisect.bisect_right(S, x)
        t = bisect.bisect_right(T, x)

        # calculate distances
        d = 10 ** 18
        for s1 in [S[s - 1], S[s]]:
            for t1 in [T[t - 1], T[t]]:
                d = min(d, abs(x - s1) + abs(s1 - t1))
        for t1 in [T[t - 1], T[t]]:
            for s1 in [S[s - 1], S[s]]:
                d = min(d, abs(x - t1) + abs(t1 - s1))

        # print result
        print(d)

if __name__ == '__main__':
    main()
