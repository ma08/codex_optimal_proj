

from sys import stdin
from operator import itemgetter

def main():
    attributes = stdin.readline().strip().split()
    songs = []
    for _ in range(int(stdin.readline())): #pylint: disable=W0612
        songs.append(stdin.readline().strip().split())
    for _ in range(int(stdin.readline())): #pylint: disable=W0612
        attribute = stdin.readline().strip()
        print(' '.join(attributes))
        for song in sorted(songs, key=itemgetter(attributes.index(attribute))):
            print(' '.join(song))
        print()

main()
