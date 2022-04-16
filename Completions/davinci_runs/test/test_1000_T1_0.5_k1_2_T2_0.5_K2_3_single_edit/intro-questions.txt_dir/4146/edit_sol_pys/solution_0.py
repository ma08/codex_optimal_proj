#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-06-17 16:48:29
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 1 of python challenge
# 
# 思路：这题和之前的一题有点像，需要计算出需要替换的位置，替换的方法是和第一个位置的数字不同的情况
#       然后统计出不同的个数，就是需要替换的数字个数

# level 1 of python challenge

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # The number of elements that need to be replaced is the number of elements
    # that are different from the first element.
    print(n - a.count(a[0]))


if __name__ == '__main__':
    main()
