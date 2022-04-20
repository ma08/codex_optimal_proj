#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


input_str = input()

is_palindrome = True
for i in range(int(len(input_str) / 2)):
    if input_str[i] != input_str[-i - 1]:
        is_palindrome = False

if is_palindrome:
    print('Yes')
else:
    print('No')
