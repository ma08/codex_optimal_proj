
# -*- coding: utf-8 -*-
# 自动化测试工程师培训第一周作业
# 1、编写一个函数，输入参数为一个字符串，输出这个字符串中最长的非重复子串的长度。（比如，输入为“abcabcbb”，输出为3，输入为“bbbbb”，输出为1。）
def longest_substring(input_str):
    if not input_str:
        return 0
    max_len = 0
    sub_str = ''
    for s in input_str:
        if s in sub_str:
            index = sub_str.index(s)
            sub_str = sub_str[index+1:] + s
        else:
            sub_str += s
        max_len = max(max_len, len(sub_str))
    return max_len


# 2、编写一个函数，输入参数为一个字符串，输出这个字符串中最长的回文子串的长度。（比如，输入为“babad”，输出为3，输入为“cbbd”，输出为2。）
def longest_palindrome(input_str):
    if not input_str:
        return 0
    max_len = 0
    for i in range(len(input_str)):
        for j in range(i+1, len(input_str)+1):
            if input_str[i:j] == input_str[i:j][::-1]:
                max_len = max(max_len, j-i)
    return max_len


# 3、编写一个函数，输入参数为一个字符串，输出这个字符串中最长的非重复子串的起始下标和长度。（比如，输入为“abcabcbb”，输出为(0,3)，输入为“bbbbb”，输出为(0,1)。）
def longest_substring_index(input_str):
    if not input_str:
        return 0
    max_len = 0
    sub_str = ''
    index = 0
    for i in range(len(input_str)):
        s = input_str[i]
        if s in sub_str:
            cur_len = len(sub_str)
            if cur_len > max_len:
                max_len = cur_len
                index = i - max_len
            sub_str = sub_str[sub_str.index(s)+1:] + s
        else:
            sub_str += s
    cur_len = len(sub_str)
    if cur_len > max_len:
        max_len = cur_len
        index = len(input_str) - max_len
    return index, max_len


# 4、编写一个函数，输入参数为一个字符串，输出这个字符串中最长的回文子串的起始下标和长度。（比如，输入为“babad”，输出为(0,3)，输入为“cbbd”，输出为(1,2)。）
def longest_palindrome_index(input_str):
    if not input_str:
        return 0
    max_len = 0
    index = 0
    for i in range(len(input_str)):
        for j in range(i+1, len(input_str)+1):
            if input_str[i:j] == input_str[i:j][::-1]:
                cur_len = j - i
                if cur_len > max_len:
                    max_len = cur_len
                    index = i
    return index, max_len


# 5、编写一个函数，输入参数为两个字符串，输出这两个字符串的最长的公共子串的长度。（比如，输入为“abcde”和“cde”，输出为3，输入为“abc”和“cde”，输出为0。）
def longest_common_substring(input_str1, input_str2):
    if not input_str1 or not input_str2:
        return 0
    len1 = len(input_str1)
    len2 = len(input_str2)
    dp = [[0]*(len2+1) for _ in range(len1+1)]
    res = 0
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if input_str1[i-1] == input_str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                res = max(res, dp[i][j])
    return res


# 6、编写一个函数，输入参数为两个字符串，输出这两个字符串的最长的公共子串的起始下标和长度。（比如，输入为“abcde”和“cde”，输出为(2,3)，输入为“abc”和“cde”，输出为(0,0)。）
def longest_common_substring_index(input_str1, input_str2):
    if not input_str1 or not input_str2:
        return 0
    len1 = len(input_str1)
    len2 = len(input_str2)
    dp = [[0]*(len2+1) for _ in range(len1+1)]
    res = 0
    index = 0
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if input_str1[i-1] == input_

import sys

def main():
    n = int(sys.stdin.readline().strip())
    temp = [int(i) for i in sys.stdin.readline().strip().split()]
    max_temp = []
    for i in range(len(temp)-2):
        max_temp.append(max(temp[i], temp[i+1], temp[i+2]))
    index = max_temp.index(min(max_temp))
    print(index+1, max_temp[index])

if __name__ == '__main__':
    main()
