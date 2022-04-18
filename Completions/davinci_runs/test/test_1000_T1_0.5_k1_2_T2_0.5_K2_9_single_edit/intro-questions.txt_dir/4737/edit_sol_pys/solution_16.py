
import fileinput


def main():
    lines = fileinput.input()
    N, p = map(int, lines[0].split())
    estimations = list(map(int, lines[1].split()))

    # The optimal solution is to solve the first problem, then the second
    # problem, etc. Any other order will be worse.
    _, penalty = solve(estimations, 0)
    if p == 0:
        print(N, penalty)

    else:
        print(0, 0)

def solve(estimations, start):
    """
    Solves the problem of solving `estimations` problems, starting with `start`.
    Returns a tuple of the number of problems solved and the penalty time.
    """
    N = len(estimations)
    if start == N:
        return 0, 0

    # If the first problem is not solvable, then there is no solution.
    if estimations[start] > 300:
        return 0, 0

    # Try solving the first problem, and then solving the rest of the problems.
    num_ac_1, penalty_1 = solve(estimations, start + 1)

    # Try skipping the first problem, and then solving the rest of the problems.
    num_ac_2, penalty_2 = solve(estimations, start + 2)

    # Choose the better of the two.
    if num_ac_1 + 1 > num_ac_2:
        return num_ac_1 + 1, penalty_1 + estimations[start]
    else:
        return num_ac_2, penalty_2


if __name__ == '__main__':
    main()
