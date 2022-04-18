

import sys

def main():
    n = int(sys.stdin.readline())
    students = [int(x) for x in sys.stdin.readline().split()]
    students.sort()
    print(students)
    max_diff = 0
    for i in range(n-1):
        diff = students[i+1] - students[i]
        if diff > max_diff:
            max_diff = diff
    print(max_diff)

if __name__ == "__main__":
    main()
