#!/usr/bin/python3

import sys

def main():
    n = int(sys.stdin.readline().strip()) # number of songs
    e = int(sys.stdin.readline().strip()) # number of events
    songs = set() # set of songs
    for i in range(e): # for each event
        line = sys.stdin.readline().strip().split() # read the event
        k = int(line[0]) # number of songs played
        for j in range(k): # for each song
            songs.add(line[j]) # add to set
    for i in range(1, n + 1): # for each song
        print(i) # print if not in set

main()
