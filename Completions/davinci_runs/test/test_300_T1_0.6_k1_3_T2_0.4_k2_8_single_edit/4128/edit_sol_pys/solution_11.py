import sys
from collections import defaultdict

def get_input():
    input_lines = sys.stdin.readlines()
    num_cases = int(input_lines[0])
    case_lines = input_lines[1:]
    case_lines = [line.strip() for line in case_lines]
    return num_cases, case_lines


def solve(case):
    num_students, num_pairs, students = case
    students = students.split(" ")
    students = [int(student) for student in students]
    students.sort()
    pairs = defaultdict(list)
    for i in range(num_students):
        pairs[students[i]].append(i)
    pairs = pairs.values()
    pairs = [pair for pair in pairs if len(pair) > 1]
    pairs = sorted(pairs, key=lambda pair: pair[1] - pair[0])
    pairs = pairs[::-1]
    print(pairs)
    for pair in pairs:
        for i in range(len(pair)):
            student = pair[i]
            if student + 1 in students:
                students.remove(student + 1)
            elif student - 1 in students:
                students.remove(student - 1)
            else:
                return "NO"
    return "YES"


def print_result(result):
    print(result)


def main():
    num_cases, cases = get_input()
    for i in range(num_cases):
        num_students, num_pairs, students = cases[i].split(" ")
        num_students = int(num_students)
        num_pairs = int(num_pairs)
        result = solve((num_students, num_pairs, students))
        print_result(result)


if __name__ == "__main__":
    main()
