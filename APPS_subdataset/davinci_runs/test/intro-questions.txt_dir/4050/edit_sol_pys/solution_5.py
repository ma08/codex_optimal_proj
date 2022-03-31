#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
    n = int(sys.stdin.readline())
    arr = [int(x) for x in sys.stdin.readline().split()] # list of numbers
    result = []
    i = 0 # index of current number
    while i < n: # iterate through all numbers
        j = i + 1 # index of next number
        while j < n: # iterate through all numbers after current number
            if arr[i] == arr[j]: # if current number equals next number
                result.append([i, j]) # add current and next number to result
                i = j # set current number to next number
                j = i + 1 # set next number to number after next number
            else: # if current number does not equal next number
                j += 1 # increment next number
        result.append([i, i]) # add current number to result
        i += 1 # increment current number
    print(len(result))
    for r in result:
        print(str(r[0] + 1) + " " + str(r[1] + 1)) # print result

if __name__ == "__main__":
    main()
