

def main():
    """
    Main program.
    """
    # Initialize the number of problems solved
    problems_solved = []
    # Read in the number of problems solved
    while True:
        problem = input()
        if problem == "-1":
            break
        problems_solved.append(problem)
    # Initialize the number of problems solved
    number_of_problems_solved = 0
    # Process the number of problems solved
    for i in range(len(problems_solved)):
        # If the problem was solved, increment the number of problems solved
        if problems_solved[i] == "1":
            number_of_problems_solved += 1
    # Print the number of problems solved
    print(number_of_problems_solved)

if __name__ == "__main__":
    main()
