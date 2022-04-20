# -*- coding: utf-8 -*-

import sys

N, K = map(int, sys.stdin.readline().split())
S = list(sys.stdin.readline().rstrip())


def calc(S, N, K):
    if K == 1:
        return "".join(sorted(S))

    S = list(sorted(S))
    ans = ""
    for i in range(N):
        ans += S.pop()
        if i < N - 1:
            if S[-1] > ans[-1]:
                ans += S.pop()
                if i < N - 2:
                    if S[-1] > ans[-1]:
                        ans += S.pop()
                        if i < N - 3:
                            if S[-1] > ans[-1]:
                                ans += S.pop()

    return ans


print(calc(S, N, K))
