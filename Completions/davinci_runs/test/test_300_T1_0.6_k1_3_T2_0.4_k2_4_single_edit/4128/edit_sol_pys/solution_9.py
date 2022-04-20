
import math
import sys

def get_input():
    input_lines = sys.stdin.readlines()
    num_cases = int(input_lines[0].strip())
    cases = []
    for i in range(num_cases):
        case = int(input_lines[i + 1].strip()) - 1
        cases.append(case)
    return cases


def solve(n):
    num_digits = math.floor(math.log10(n)) + 1
    if num_digits == 1:
        return n
    if num_digits == 2:
        return 9
    if num_digits == 3:
        return 9 + (n - 99)
    if num_digits == 4:
        return 9 + 900
    if num_digits == 5:
        return 9 + 900 + (n - 9999)
    return 9 + 900 + 90000


def print_result(results):
    for result in results:
        print(result)


def main():
    cases = get_input()
    results = []
    for case in cases:
        result = solve(case)
        results.append(result)
    print_result(results)


if __name__ == "__main__":
    main()
