

def main():
    """
    Main program.
    """
    # Initialize the submissions log and the number of problems solved.
    submissions_log = []
    problems_solved = 0
    # Read in the submissions log.
    while True:
        submission = input()
        if submission == "-1":
            break
        submissions_log.append(submission.split())
    # Initialize the time score.
    time_score = 0
    for i, submission in enumerate(submissions_log):
        # If the submissions is correct, add the time to the time score.
        if submission[2] == "right":
            time_score += int(submission[0])
            problems_solved += 1
        # If the submissions is wrong, check if the problem was solved.
        else:
            # If the problem was solved, add the penalty to the time score.
            if submission[1] in [submissions_log[j][1] for j in range(i) if submissions_log[j][2] == "right"]:
                time_score += 20
    # Print the number of problems solved and the time score.
    print(problems_solved, time_score)

if __name__ == "__main__":
    main()
