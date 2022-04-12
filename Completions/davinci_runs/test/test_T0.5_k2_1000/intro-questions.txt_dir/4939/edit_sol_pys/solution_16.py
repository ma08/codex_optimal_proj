
import sys

def main():
    n = int(sys.stdin.readline())
    commands = sys.stdin.readline().split()
    student = 0
    undo = []
    for command in commands:
        if command == "undo":
            student = undo.pop() % n
        else:
            student = (student + int(command)) % n
            undo.append(student)
    print(student)

main()
