

from sys import stdin
from operator import itemgetter

def main():
    attrs = stdin.readline().strip().split()
    songs = []
    for _ in range(int(stdin.readline())):
        songs.append(stdin.readline().strip().split())
    for _ in range(int(stdin.readline())):
        attr = stdin.readline().strip()
        print(attrs.join(' '))
        for song in sorted(songs, key=itemgetter(attrs.index(attr))):
            print(song.join(' '))
        print()

main()
