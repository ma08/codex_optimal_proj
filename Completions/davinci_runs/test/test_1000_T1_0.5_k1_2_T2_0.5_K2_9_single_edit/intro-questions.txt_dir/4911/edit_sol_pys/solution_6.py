

from sys import stdin
from itertools import islice
from operator import itemgetter

def main():
    attributes = next(stdin).rstrip().split()
    n_songs = int(next(stdin))
    songs = [dict(zip(attributes, next(stdin).rstrip().split())) for _ in xrange(n_songs)]
    n_commands = int(next(stdin))
    commands = list(islice(stdin, n_commands))
    print(' '.join(attributes))
    for command in commands:
        songs.sort(key=itemgetter(command.rstrip()))
        print('\n'.join(' '.join(song[attr] for attr in attributes) for song in songs))
        print()

main()
