#!/usr/bin/env python

from sys import stdin
from operator import itemgetter

def main():
    attrs = stdin.readline().strip().split()[1:]
    songs = []
    for _ in range(int(stdin.readline())):
        songs.append(stdin.readline().strip().split()[1:])
    for _ in range(int(stdin.readline())):
        attr = stdin.readline().strip()
        print(' '.join(attrs), end='')
        for song in sorted(songs, key=itemgetter(attrs.index(attr))):
            print(' '.join(song), end='')
        print()

main()
