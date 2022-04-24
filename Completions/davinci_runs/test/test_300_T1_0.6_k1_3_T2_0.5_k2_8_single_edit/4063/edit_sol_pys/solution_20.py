def main():
    # Read the number of problems, N
    N = int(input())

    # Read the difficulty of each problem, problems
    problems = [int(x) for x in input().split()]

    # Sort the problems in ascending order
    problems.sort()

    # Calculate the number of problems for each difficulty
    problems_by_difficulty = {}
    for problem in problems:
        if problem not in problems_by_difficulty:
            problems_by_difficulty[problem] = 0
        problems_by_difficulty[problem] += 1

    # Calculate the number of choices of the integer K
    count = 0
    for difficulty in problems_by_difficulty:
        if difficulty in problems_by_difficulty:
            count += problems_by_difficulty[difficulty] * problems_by_difficulty[N//2-difficulty]

    # Print the answer
    print(count)


if __name__ == '__main__':
    main()
