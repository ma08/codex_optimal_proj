

from sys import stdin
from itertools import islice
from operator import itemgetter

def main():
    attributes = next(stdin).rstrip().split()
    n_files = int(next(stdin))
    files = [dict(zip(attributes, line.rstrip().split())) for line in islice(stdin, n_files)]
    n_commands = int(next(stdin)) 
    commands = list(islice(stdin, n_commands)) 
    print(' '.join(attributes))
    for command in commands:
        files.sort(key=itemgetter(command.rstrip()))
        print('\n'.join(' '.join(file[attr] for attr in attributes) for file in files))
        print()

main()
