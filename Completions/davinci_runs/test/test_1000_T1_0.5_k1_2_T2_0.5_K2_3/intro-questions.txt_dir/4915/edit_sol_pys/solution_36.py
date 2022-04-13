

def main():
    """
    Main program.
    """
    # Initialise the submission log and the number of problems solved.
    submission_log = []
    problems_solved = 0
    # Read in the submission log.
    while True:
        submission = input()
        if submission == "-1":
            break
        submission_log.append(submission.split())
    # Initialise the time score.
    time_score = 0
    # Process the submission log.
        # If the submission is wrong, check if the problem was solved.
        if submission_log[i][2] == "wrong":
            # If the problem was solved, add the penalty to the time score.
            if submission_log[i][1] in [submission_log[j][1] for j in range(i) if submission_log[j][2] == "right"]:
                time_score += 20
    for i in range(len(submission_log)):
        # If the submission is correct, add the time to the time score.
        else:
            time_score += int(submission_log[i][0])
            problems_solved += 1
    # Print the number of problems solved and the time score
    print(problems_solved, time_score)

if __name__ == "__main__":
    main()
