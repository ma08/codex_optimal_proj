
import sys

def get_input():
    input_lines = sys.stdin.readlines()
    num_cases = int(input_lines[0])
    cases = []
    for i in range(num_cases):
        case = int(input_lines[i + 1])
        cases.append(case)
    return cases


def solve(n):
    if n < 4:
        return 0
    if n % 2 == 1:
        return int(n / 2)
    return int(n / 2 - 1)


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
