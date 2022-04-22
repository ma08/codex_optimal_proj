

# -*- coding: utf-8 -*-

def main():
    from sys import stdin
    from itertools import accumulate


    from bisect import bisect_left

    readline = stdin.readline

    D, G = map(int, readline().split())
    P, C = zip(*[map(int, readline().split()) for _ in range(D)])
    P = list(P)
    C = list(C)
    P_cum = list(accumulate([0] + P))
    P_cum.pop(0)
    C_cum = list(accumulate([0] + C))
    C_cum.pop(0)

    # O(D^2)
    # ans = 10**10
    # for i in range(2**D):
    #     score = 0
    #     cnt = 0
    #     for j in range(D):
    #         if i >> j & 1:
    #             score += 100 * (j + 1) * P[j] + C[j]
    #             cnt += P[j]
    #     for j in range(D - 1, -1, -1):
    #         if score >= G:
    #             ans = min(ans, cnt)
    #             break
    #         if i >> j & 1:
    #             continue
    #         for k in range(P[j]):
    #             if score >= G:
    #                 break
    #             score += 100 * (j + 1)
    #             cnt += 1
    #     else:
    #         ans = min(ans, cnt)
    # print(ans)

    # O(D)
    ans = 10**10
    for i in range(D):
        score = C_cum[i] + 100 * (i + 1) * P_cum[i]
        if score >= G:
            ans = min(ans, P_cum[i])
        else:
            cnt = P_cum[i]
            score += 100 * (i + 1) * (P_cum[-1] - P_cum[i])
            cnt += (P_cum[-1] - P_cum[i])
            if score >= G:
                ans = min(ans, cnt)
            else:
                idx = bisect_left(C_cum[i + 1:], G - score)
                ans = min(ans, cnt + idx)
    print(ans)


if __name__ == '__main__':
    main()
