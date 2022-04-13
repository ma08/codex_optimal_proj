

from sys import stdin
from itertools import islice
from operator import itemgetter

def main():
    attributes = next(stdin).rstrip().split()
    n_lines = int(next(stdin))
    lines = [dict(zip(attributes, next(stdin).rstrip().split())) for _ in range(n_lines)]
    n_commands = int(next(stdin)) + 1
    commands = list(islice(stdin, n_commands))[1:]
    print(' '.join(attributes))
    for command in commands:
        lines.sort(key=itemgetter(command.rstrip()))
        print('\n'.join(' '.join(line[attr] for attr in attributes) for line in lines))
        print()

main()
