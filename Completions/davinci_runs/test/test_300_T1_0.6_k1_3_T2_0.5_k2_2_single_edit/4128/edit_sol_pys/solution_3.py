import sys
from collections import Counter

def get_input():
    input_lines = sys.stdin.readlines()
    num_strings = int(input_lines[0].strip())
    return input_lines[1:num_strings + 1]


def solve(s):
    s_counter = Counter(s)
    for key in s_counter:
        if s_counter[key] > 1:
            return "no"
    return "yes"


def print_result(results):
    for result in results:
        print(result)


def main():
    cases = get_input()
    results = []
    for string in cases:
        result = solve(string)
        results.append(result)
    print_result(results)


if __name__ == "__main__":
    main()
