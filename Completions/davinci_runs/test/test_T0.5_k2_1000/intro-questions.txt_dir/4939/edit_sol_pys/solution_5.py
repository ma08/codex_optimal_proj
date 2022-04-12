#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    commands = sys.stdin.readline().split()
    student = 0
    undo = [0]
    for command in commands:
        if command == "undo":
            undo.pop()
            student = undo[-1]
        else:
            student = (student + int(command))
            student %= n
            undo.append(student)
    print(student)

main()
