

import sys
import math

s = input().rstrip()
k = int(input())

def calc_length(s):
    length = 0
    for char in s:
        if char == '1':
            length += 1
        else:
            length += 10**(int(char)-1)
    return length

def calc_result(s, k):
    length = 0
    result = ''
    for char in s:
        if char == '1':
            length += 1
            if length == k:
                result = '1'
                break
        else:
            length += 10**(int(char)-1)
            if length >= k:
                for i in range(int(char)):
                    result += char
                    if length - 10**i == k:
                        break
                    elif length - 10**i > k:
                        result = result[:-1]
                        break
                break
    return result

print(calc_result(s, k))