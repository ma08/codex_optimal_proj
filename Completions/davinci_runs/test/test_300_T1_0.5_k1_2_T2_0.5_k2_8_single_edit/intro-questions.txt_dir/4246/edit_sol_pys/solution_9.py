#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:41:54 2019


@author: jakub
"""


def hammingDistance(s, t):
    correct = 0

    for i in range(len(s)):
        if s[i] == t[i]:
            correct += 1

    return correct


if __name__ == '__main__':
    s = input()
    t = input()

    print(hammingDistance(s, t))
