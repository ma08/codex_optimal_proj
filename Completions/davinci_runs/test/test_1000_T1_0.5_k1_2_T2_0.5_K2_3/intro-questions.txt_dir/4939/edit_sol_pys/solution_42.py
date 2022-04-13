import sys

def main():
    n, k = map(int, input().split())
    commands = input().split()
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
