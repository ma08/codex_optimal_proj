import sys
import math

def get_input():
    input_lines = sys.stdin.readlines()
    num_cases = int(input_lines[0].strip())
    cases = []
    for i in range(num_cases):
        case = int(input_lines[i + 1].strip())
        cases.append(case)
    return cases


def solve(n):
    num_squares = int(math.sqrt(n))
    return num_squares


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
