


def main():
    # Read the number of problems and the number of days
    N, D = [int(x) for x in input().split()]

    # Read the difficulty of each problem and the deadline of each problem
    problems = []
    for i in range(N):
        problems.append([int(x) for x in input().split()])

    # Sort the problems in ascending order of deadline
    problems.sort(key=lambda x: x[1])

    # Calculate the number of problems for each difficulty and deadline
    problems_by_difficulty_and_deadline = {}
    for i in range(N):
        if problems[i][0] not in problems_by_difficulty_and_deadline:
            problems_by_difficulty_and_deadline[problems[i][0]] = {}
        if problems[i][1] not in problems_by_difficulty_and_deadline[problems[i][0]]:
            problems_by_difficulty_and_deadline[problems[i][0]][problems[i][1]] = 0
        problems_by_difficulty_and_deadline[problems[i][0]][problems[i][1]] += 1

    # Calculate the number of choices of the integer K and the deadline
    count = 0
    for difficulty in problems_by_difficulty_and_deadline:
        for deadline in problems_by_difficulty_and_deadline[difficulty]:
            if difficulty in problems_by_difficulty_and_deadline:
                count += problems_by_difficulty_and_deadline[difficulty][deadline] * problems_by_difficulty_and_deadline[N//2-difficulty][deadline]

    # Print the answer
    print(count)


if __name__ == '__main__':
    main()
