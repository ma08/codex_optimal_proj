import sys

def main():
    n, k = map(int, sys.stdin.readline().split()) # n is the number of students, k is the number of commands
    commands = sys.stdin.readline().split()
    student = 0 # current student
    undo = [] # list of previous students
    for command in commands:
        # if the command is undo, the current student is the previous student
        if command == "undo":
            student = undo.pop()
        else: # if the command is a number, add that number to the current student and mod by the number of students
            student = (student + int(command)) % n
            undo.append(student) # add the current student to the undo list
    print(student)

main()
