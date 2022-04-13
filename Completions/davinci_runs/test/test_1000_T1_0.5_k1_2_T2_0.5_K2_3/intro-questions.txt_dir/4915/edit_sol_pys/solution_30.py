import sys


def main():
    """
    Main function that reads in input and outputs the solution
    """
    problems = {} # dictionary of problems
    current_time = 0 # current time

    # read in input
    for line in sys.stdin:
        if line.strip() == '-1': # parse line
            break

        # parse line
            break
        time, problem, result = line.strip().split()
        time = int(time)

        # add problem to dictionary if not exist
        current_time = time
        if problem not in problems:

        # update problem information
            problems[problem] = {'solved': False, 'penalty': 0, 'last_submit': current_time}
        if result == 'right':
            problems[problem]['solved'] = True
            problems[problem]['last_submit'] = current_time
        else:
            problems[problem]['penalty'] += 20

    # calculate and output solution
    solved = sum([1 if problem['solved'] else 0 for problem in problems.values()])
    penalty = sum([problem['penalty'] for problem in problems.values()])
    submit_time = sum([problem['last_submit'] for problem in problems.values() if problem['solved']])
    print(solved, submit_time + penalty)


if __name__ == '__main__':
    main()
