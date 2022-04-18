# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#

import sys

class Song:
    def __init__(self, attr):
        self.attr = attr
    def __repr__(self):
        return ' '.join(self.attr)

def stable_sort(songs, attribute):
    return sorted(songs, key=lambda song: song.attr[attribute])

def main():
    attributes = sys.stdin.readline().strip().split()
    m = int(sys.stdin.readline())
    songs = []
    for _ in range(m):
        songs.append(Song(sys.stdin.readline().strip().split()))
    n = int(sys.stdin.readline())
    for _ in range(n):
        attribute = sys.stdin.readline().strip()
        print(' '.join(attributes))
        for song in stable_sort(songs, attributes.index(attribute)):
            print(song)
        print()

if __name__ == '__main__':
    main()
