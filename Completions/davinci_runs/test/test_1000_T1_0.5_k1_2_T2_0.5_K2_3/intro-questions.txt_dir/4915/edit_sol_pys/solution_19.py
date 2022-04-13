

def main():
    """
    Main function.
    """
    # Read the input
    input_lines = []
    while True:
        line = input()
        if line == '-1':
            break
        input_lines.append(line)

    # Split the input into a list
    input_list = [line.split() for line in input_lines]

    # Create a dictionary to hold the problem and the time to solve it
    problem_dict = {}
    for entry in input_list:
        problem_dict[entry[1]] = int(entry[0])

    # Create a dictionary to hold the problem and the number of attempts
    attempts_dict = {}
    for entry in input_list:
        if entry[1] not in attempts_dict.keys():
            attempts_dict[entry[1]] = 0
        attempts_dict[entry[1]] += 1

    # Create a dictionary to hold the problem and the number of right/wrong attempts
    right_wrong_dict = {}
    for entry in input_list:
        if entry[1] not in right_wrong_dict.keys():
            right_wrong_dict[entry[1]] = 0
        if entry[2] == 'right':
            right_wrong_dict[entry[1]] += 1
        else:
            right_wrong_dict[entry[1]] -= 1

    # Create a dictionary to hold the problem and the penalty
    penalty_dict = {}
    for key, value in right_wrong_dict.items():
        if value > 0:
            penalty_dict[key] = (attempts_dict[key] - 1) * 20
        else:
            penalty_dict[key] = 0

    # Create a dictionary to hold the problem and the time to solve it with penalty
    time_penalty_dict = {}
    for key, value in problem_dict.items():
        time_penalty_dict[key] = value + penalty_dict[key]

    # Create a list of all of the problems that were solved
    solved_list = []
    for key, value in right_wrong_dict.items():
        if value > 0:
            solved_list.append(key)

    # Calculate the number of problems solved and the total time measure
    number_of_problems_solved = len(solved_list)
    total_time_measure = sum([time_penalty_dict[problem] for problem in solved_list])

    # Output the results
    print(str(number_of_problems_solved) + ' ' + str(total_time_measure))

if __name__ == '__main__':
    main()
