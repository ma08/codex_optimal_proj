#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/21
# @Author  : Edrain


def main():
    n = int(input())  # 总人数
    a = [[] for _ in range(n)]  # a是一个二维数组，有n个元素，每个元素是一个空数组
    for i in range(n):  # 读入数据
        a[i] = list(map(int, input().split()))  # 把数据转换为整数，并放入a中
    for i in range(n):  # 编号减1
        a[i][0] -= 1
        a[i][1] -= 1
    for i in range(n):  # 去除重复的元素
        if len(a[i]) == 2:
            j = a[i][0]
            if a[j][0] == i:
                a[j][0] = a[j][1]
                a[j].pop()
            else:
                a[j][1] = a[j][0]
                a[j][0] = i
            if a[j][0] == j:
                a[j].pop()
            a[i].pop()
    for i in range(n):  # 将a中的每个元素变为一个整数
        a[i] = a[i][0]
    ans = [0] * n  # ans是一个长度为n的数组
    for i in range(n):  # ans赋值
        ans[i] = i + 1
    for i in range(n):  # 根据a中的数据，交换ans中的元素
        j = a[i]
        ans[i], ans[j] = ans[j], ans[i]
    print(*ans)  # 输出ans


if __name__ == '__main__':
    main()
