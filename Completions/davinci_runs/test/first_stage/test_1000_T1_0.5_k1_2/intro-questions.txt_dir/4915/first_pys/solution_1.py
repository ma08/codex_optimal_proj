

def main():
    """
    Main program.
    """
    # Initialize the submission log and the number of problems solved.
    submission_log = []
    problems_solved = 0
    # Read in the submission log.
    while True:
        submission = input()
        if submission == "-1":
            break
        submission_log.append(submission.split())
    # Initialize the time score.
    time_score = 0
    # Process the submission log.
    for i in range(len(submission_log)):
        # If the submission is correct, add the time to the time score.
        if submission_log[i][2] == "right":
            time_score += int(submission_log[i][0])
            problems_solved += 1
        # If the submission is wrong, check if the problem was solved.
        else:
            # If the problem was solved, add the penalty to the time score.
            if submission_log[i][1] in [submission_log[j][1] for j in range(i) if submission_log[j][2] == "right"]:
                time_score += 20
    # Print the number of problems solved and the time score.
    print(problems_solved, time_score)

if __name__ == "__main__":
    main()