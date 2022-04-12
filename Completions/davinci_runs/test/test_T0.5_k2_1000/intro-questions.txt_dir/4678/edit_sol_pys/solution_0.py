#!/usr/bin/env python3

import sys

def main():
    num_people = int(sys.stdin.readline()) # number of people
    heights = [int(x) for x in sys.stdin.readline().split()] # heights of people
    stools = [0 for i in range(num_people)] # number of stools each person needs
    current_max = 0 # current max height
    for i in range(num_people): # for each person
        stools[i] = max(current_max, heights[i]) # set the number of stools to the max of the current max height and the current person's height
        current_max = stools[i] # update the current max height
    print(sum(stools)) # print the sum of the number of stools needed

main()
