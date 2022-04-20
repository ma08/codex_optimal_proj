#!/usr/bin/python3

import sys

N = int(input())

def count_moves(n):
    moves = 0

    for i in range(1,n+1):
        if(i*i >= n):
            moves = i
            break

    return 2*moves-2

print(count_moves(N))
