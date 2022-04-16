

import sys


def main():
    n, k = map(int, sys.stdin.readline().strip().split())
    commands = sys.stdin.readline().strip().split()
    egg = 0
    for command in commands:
        if command == 'undo':
            k -= 1
            if k == 0:
                break
            continue
        command = int(command)
        egg = (egg + command) % n
        if egg < 0:
            egg += n
    print(egg)


main()
