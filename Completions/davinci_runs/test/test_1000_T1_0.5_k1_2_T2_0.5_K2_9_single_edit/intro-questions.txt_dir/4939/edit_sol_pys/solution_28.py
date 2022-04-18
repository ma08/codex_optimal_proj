

import sys

def main():
    n, k = map(int, input().split())
    commands = input().split()
    student = 0
    undo = []
    for command in commands:
        if command == "undo":
            student = undo.pop()
        else:
            student = (student + int(command)) % n
            undo.append(student)
    print(student)

main()
