from sys import stdin
from operator import itemgetter

def main():
    attributes = stdin.readline().strip().split()
    songs = []
    for _ in range(int(stdin.readline())):
        songs.append(stdin.readline().strip().split())
    for _ in range(int(stdin.readline())):
        attribute = stdin.readline().strip()
        print(' '.join(attributes), end='\n')
        for song in sorted(songs, key=itemgetter(attributes.index(attribute))):
            print(' '.join(song), end='\n')
        print(end='\n')

main()
