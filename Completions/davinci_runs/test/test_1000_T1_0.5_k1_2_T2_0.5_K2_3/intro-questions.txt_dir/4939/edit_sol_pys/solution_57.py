import sys

def main():
    n, k = map(int, sys.stdin.readline().strip().split())
    commands = sys.stdin.readline().strip().split()
    egg = 0
    for command in commands:
        if command == 'undo' and k != 0:
            k -= 1
            egg = int(sys.stdin.readline().strip())
            continue
        command = int(command)
        egg = (egg + command) % n
        if egg < 0:
            egg += n
    print(egg)

main()
