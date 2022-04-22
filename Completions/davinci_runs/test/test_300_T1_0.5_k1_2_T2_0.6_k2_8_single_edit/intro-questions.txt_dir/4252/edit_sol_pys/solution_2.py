#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# n = int(input())
# s = input()
# print(len(s.replace("xxx", "")))

def get_result(n, s):
    return len(s.replace("xxx", ""))


if __name__ == "__main__":
    n = int(input())
    s = input()
    print(get_result(n, s))
