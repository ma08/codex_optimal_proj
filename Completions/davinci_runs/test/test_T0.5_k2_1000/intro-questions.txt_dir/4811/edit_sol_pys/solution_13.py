#!/usr/bin/env python3

def get_bar_size(k): return 2 ** (len(bin(k)) - 3)

def get_num_breaks(k): return len(bin(k)) - 3

k = int(input())
print('{} {}'.format(get_bar_size(k), get_num_breaks(k)))
