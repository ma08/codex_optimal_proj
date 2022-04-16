

from sys import stdin
from itertools import islice
from operator import itemgetter

def main():
    attributes = stdin.readline().rstrip().split()
    n_songs = int(stdin.readline())
    songs = [dict(zip(attributes, stdin.readline().rstrip().split())) for _ in range(n_songs)]
    n_commands = int(stdin.readline())
    commands = list(islice(stdin, n_commands))
    print(' '.join(attributes))
    for command in commands:
        songs.sort(key=itemgetter(command.rstrip()))
        print('\n'.join(' '.join(song[attr] for attr in attributes) for song in songs))
        print()

main()
