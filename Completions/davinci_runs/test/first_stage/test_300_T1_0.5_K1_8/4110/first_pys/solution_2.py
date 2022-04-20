

import sys

def main():
    # Read lines from stdin
    lines = [line.strip() for line in sys.stdin]

    # Parse input
    D, G = map(int, lines[0].split())
    p_c = [list(map(int, line.split())) for line in lines[1:]]

    # Solve
    print(solve(D, G, p_c))

def solve(D, G, p_c):
    # Number of problems to solve
    num_problems = 0

    # Current total score
    total_score = 0

    # Solve all problems with the highest score
    max_score = 100 * D
    max_score_idx = D
    while total_score < G and max_score_idx > 0:
        num_problems += p_c[max_score_idx - 1][0]
        total_score += max_score * p_c[max_score_idx - 1][0]
        max_score_idx -= 1

    # Solve problems with the second highest score, if necessary
    if total_score < G:
        # Calculate how many problems must be solved in order to reach G points
        num_problems_needed = (G - total_score) // 100 + 1
        num_problems += min(num_problems_needed, p_c[max_score_idx][0])
        total_score += min(num_problems_needed, p_c[max_score_idx][0]) * 100

    # Add perfect bonus, if necessary
    if total_score < G:
        total_score += p_c[max_score_idx][1]

    return num_problems

if __name__ == '__main__':
    main()