from sys import stdin
from operator import itemgetter

def main():
    attrs = stdin.readline().strip().split()
    songs = []
    for _ in range(int(stdin.readline().strip())):
        songs.append(stdin.readline().strip().split())
    for _ in range(int(stdin.readline().strip())):
        attr = stdin.readline().strip()
        print(' '.join(attrs))
        for song in sorted(songs, key=itemgetter(attrs.index(attr))):
            print(' '.join(song))
        print()

main()
