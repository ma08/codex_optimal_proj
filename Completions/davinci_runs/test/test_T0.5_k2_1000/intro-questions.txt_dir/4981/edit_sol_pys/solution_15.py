#!/usr/bin/env python3

import sys

def main():
    input_list = sys.stdin.readline().strip().split() # read input
    input_list = [int(i) for i in input_list] # convert to int
    order = sys.stdin.readline().strip() # read the order of the output
    input_list = sorted(input_list) # sort the input
    for i in order: # print the output
        print(input_list.pop(0), end=' ') # pop the first element of the list

main()
