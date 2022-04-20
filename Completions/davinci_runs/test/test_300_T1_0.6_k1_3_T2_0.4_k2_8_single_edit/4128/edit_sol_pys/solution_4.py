import sys

def get_input():
    input_lines = sys.stdin.readlines()
    num_cases = int(input_lines[0].strip())
    cases = []
    for case in range(1, num_cases + 1):
        num_piles = int(input_lines[case].strip())
        piles = []
        for pile in range(num_piles):
            piles.append(int(input_lines[case + pile + 1].strip()))
        cases.append(piles)
    return cases


def solve(piles):
    return


def print_result(results):
    for i, result in enumerate(results):
        print("Case #{}: {}".format(i + 1, result))
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
