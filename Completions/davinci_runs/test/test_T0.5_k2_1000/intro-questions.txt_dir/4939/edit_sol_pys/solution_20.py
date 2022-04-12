import sys

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        k = int(sys.stdin.readline())
        commands = sys.stdin.readline().split()
        student = 0
        undo = []
        for command in commands:
            if command == "undo":
                student = undo.pop()
            else:
                student = (student + int(command)) % k
                undo.append(student)
        print(student)

main()
