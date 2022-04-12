#!/usr/bin/env python3

import sys

def main():
    v = list(map(int, sys.stdin.readline().split())) # read line
    v.append(20) # append 20
    v.append(0) # append 0
    v.sort() # sort
    print(v[0]*v[1]*v[2]*v[3]*v[4]*v[5]*v[6]) # print

main()
