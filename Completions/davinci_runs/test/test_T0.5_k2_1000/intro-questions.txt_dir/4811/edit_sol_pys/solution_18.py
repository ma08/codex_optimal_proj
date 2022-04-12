#!/usr/bin/env python3

def get_bar_length(k):
    return 2 ** (len(bin(k)) - 3)

def get_num_cuts(k):
    bar_length = get_bar_length(k)
    num_cuts = 0
    while bar_length != k:
        bar_length //= 2
        num_cuts += 1
    return num_cuts

k = int(input())
print('{} {}'.format(get_bar_length(k), get_num_cuts(k)))
