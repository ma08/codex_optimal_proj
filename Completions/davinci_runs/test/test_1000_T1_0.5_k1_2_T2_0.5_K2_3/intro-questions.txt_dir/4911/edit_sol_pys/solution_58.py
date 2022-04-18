

import sys
import itertools
import operator

def main():
    attributes = next(sys.stdin).rstrip().split()
    n_lines = int(next(sys.stdin))
    lines = [dict(zip(attributes, next(sys.stdin).rstrip().split())) for _ in range(n_lines)]
    n_commands = int(next(sys.stdin)) + 1
    commands = list(itertools.islice(sys.stdin, n_commands))[1:]
    print(commands)
    print(' '.join(attributes))
    for command in commands:
        lines.sort(key=operator.itemgetter(command.rstrip()))
        print('\n'.join(' '.join(line[attr] for attr in attributes) for line in lines))
        print()

main()
