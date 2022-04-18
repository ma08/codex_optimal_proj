

import sys

class Song:
    def __init__(self, *attributes):
        self.attributes = list(attributes)
    def __repr__(self):
        return '\t'.join(self.attributes)

def stable_sort(songs, attribute):
    return sorted(songs, key=lambda song: song.attributes[attribute], reverse=True)

def main():
    attributes = sys.stdin.readline().strip().split()
    m = int(sys.stdin.readline())
    songs = []
    for _ in range(m):
        songs.append(Song(*sys.stdin.readline().strip().split()))
    n = int(sys.stdin.readline())
    for _ in range(n):
        attribute = sys.stdin.readline().strip()
        print('\t'.join(attributes))
        for song in stable_sort(songs, attributes.index(attribute)):
            print(song)
        print()

if __name__ == '__main__':
    main()
