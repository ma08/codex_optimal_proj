


def main():
    # Read the number of problems
    N = int(input())  # N is the number of problems
    
    # Read the difficulty of each problem
    problems = [int(x) for x in input().split()]  # problems is a list of the difficulty of each problem

    # Sort the problems in ascending order 
    problems.sort()

    # Calculate the number of problems for each difficulty
    problems_by_difficulty = {}
    for problem in problems:
    # problems_by_difficulty is a dictionary
    # Key: difficulty
    # Value: number of problems with that difficulty
        if problem not in problems_by_difficulty:
            problems_by_difficulty[problem] = 0
        problems_by_difficulty[problem] += 1

    # Calculate the number of choices of the integer K
    # count is the number of choices of the integer K
    count = 0
    # Iterate through the difficulties
    for difficulty in problems_by_difficulty:
        # If the difficulty is in the dictionary
        # The difficulty is the number of problems with that difficulty
        # N//2-difficulty is the number of problems with difficulty K-difficulty
        # Therefore, the number of choices of the integer K is the number of problems with that difficulty
        # times the number of problems with difficulty K-difficulty
        if difficulty in problems_by_difficulty:
            count += problems_by_difficulty[difficulty] * problems_by_difficulty[N//2-difficulty]

    # Print the answer
    print(count)


if __name__ == '__main__':
    main()
