#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/21
# @Author  : Edrain


def main():
    # n = int(input())
    # a = [[] for _ in range(n)]
    # for i in range(n):
    #     a[i] = list(map(int, input().split()))
    # for i in range(n):
    #     a[i][0] -= 1
    #     a[i][1] -= 1
    # for i in range(n):
    #     if len(a[i]) == 2:
    #         j = a[i][0]
    #         if a[j][0] == i:
    #             a[j][0] = a[j][1]
    #             a[j].pop()
    #         else:
    #             a[j][1] = a[j][0]
    #             a[j][0] = i
    #         if a[j][0] == j:
    #             a[j].pop()
    #         a[i].pop()
    # for i in range(n):
    #     a[i] = a[i][0]
    # ans = [0] * n
    # for i in range(n):
    #     ans[i] = i + 1
    # for i in range(n):
    #     j = a[i]
    #     ans[i], ans[j] = ans[j], ans[i]
    # print(*ans)
    a = [3, 2, 1, 4]
    b = [1, 2, 3, 4]
    a.sort(key=lambda x: b[x - 1])
    print(a)


if __name__ == '__main__':
    main()
