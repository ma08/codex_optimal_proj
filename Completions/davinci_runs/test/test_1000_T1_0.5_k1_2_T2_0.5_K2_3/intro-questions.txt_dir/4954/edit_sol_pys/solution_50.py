#!/usr/bin/env python3

import sys

def main():
    N, B, H, W = [int(x) for x in sys.stdin.readline().split()]
    minCost = B + 1
    for i in range(H): # number of hotels
        price = int(sys.stdin.readline())
        beds = [int(x) for x in sys.stdin.readline().split()] # beds per week
        for j in range(W):
            if beds[j] >= N: # enough beds
                cost = price * N
                if cost < minCost: # update min cost
                    minCost = cost
    if minCost <= B: # can go
        print(minCost)
    else:
        print("stay home")

main()
