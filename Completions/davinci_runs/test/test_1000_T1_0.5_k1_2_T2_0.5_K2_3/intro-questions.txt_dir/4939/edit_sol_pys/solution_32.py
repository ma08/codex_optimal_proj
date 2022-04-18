import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    commands = sys.stdin.readline().split()
    student = 0
    undo = []
    for command in commands:
        if command == "undo":
            student = undo.pop(0)
        else:
            undo.append(student)
            student = (student + int(command)) % n
    print(student)

main()
