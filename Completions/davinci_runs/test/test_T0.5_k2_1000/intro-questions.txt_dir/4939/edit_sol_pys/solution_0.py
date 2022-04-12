
import sys

def main():
    n, k = map(int, sys.stdin.readline().strip().split())  # n = number of eggs, k = number of undo commands
    commands = sys.stdin.readline().strip().split()
    egg = 0  # number of eggs in the basket
    for command in commands:
        if command == 'undo':  # undo the last command
            k -= 1
            if k == 0:
                break
            continue
        command = int(command)
        egg = (egg + command) % n
        if egg < 0:
            egg += n  # if the number of eggs is negative, add n to it
    print(egg)

main()
