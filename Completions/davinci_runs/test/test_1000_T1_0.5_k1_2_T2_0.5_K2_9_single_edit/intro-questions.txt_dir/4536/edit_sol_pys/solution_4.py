#!/usr/bin/env python
# -*- coding: utf-8 -*-


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    plus_one = 1
    for i in range(len(digits) - 1, -1, -1):
        if plus_one == 1:
            if digits[i] + 1 == 10:
                digits[i] = 0
            else:
                digits[i] += 1
                plus_one = 0
        else:
            break
    if plus_one == 1:
        digits.insert(0, 1)
    return digits


print(plusOne([9, 9, 9]))
