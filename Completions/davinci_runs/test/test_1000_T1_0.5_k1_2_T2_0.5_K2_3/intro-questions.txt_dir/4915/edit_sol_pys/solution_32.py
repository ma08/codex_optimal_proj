

def main():
    """
    Main program.
    """
    # Initialize the submission log, the number of problems solved, and the time score.
    submission_log, time_score = [], 0
    problems_solved = 0
    # Read in the submission log.
    while True:
        submission = input()
        if submission == "-1":
            break
    # Initialize the list of solved problems.
    solved_problems = []
        submission_log.append(submission.split())
    # Process the submission log.
    for i in range(len(submission_log)):
        # If the submission is correct, add the time to the time score.
        if submission_log[i][2] == "right":
            time_score += int(submission_log[i][0])
            problems_solved += 1
        # If the submission is wrong, check if the problem was solved.
        else:
            # If the problem was solved, add the penalty to the time score.
            if submission_log[i][1] in solved_problems:
                time_score += 20
            else:
                solved_problems.append(submission_log[i][1])
    # Print the number of problems solved and the time score.
    print(problems_solved, time_score)

if __name__ == "__main__":
    main()
