
import sys

def main():
    n = int(input())
    commands = []
    for _ in range(n):
        commands.append(input())
    for command in commands:
        if command[0:10] == "Simon says":
            print(command[10:])


main()
