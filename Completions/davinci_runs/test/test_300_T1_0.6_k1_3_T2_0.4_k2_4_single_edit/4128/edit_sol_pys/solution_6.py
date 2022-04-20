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
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True



def solve(n):
    count = 0
    for i in range(3, n, 2):
        if is_prime(i):
            count += 1
    return count


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
