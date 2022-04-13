import sys



def main():
    """
    Main function that reads in input and outputs the solution
    """
    problems = dict()
    current_time = int()
    for line in sys.stdin:
        if line.strip() == '-1':
            break
        time, problem, result = line.strip().split()
        time = int(time)
        current_time = time
        if problem not in problems:
            problems[problem] = {'solved': bool(), 'penalty': int(), 'last_submit': current_time}
        if result == 'right':
            problems[problem]['solved'] = True
            problems[problem]['last_submit'] = current_time
        else:
            problems[problem]['penalty'] += 20
    solved = sum([1 if problem['solved'] else 0 for problem in problems.values()])  # noqa
    penalty = sum([problem['penalty'] for problem in problems.values()])  # noqa
    submit_time = sum([problem['last_submit'] for problem in problems.values() if problem['solved']])  # noqa
    print(solved, submit_time + penalty)


if __name__ == '__main__':
    main()
