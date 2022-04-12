

import sys

def main():
    times = dict()
    problems = dict()
    for line in sys.stdin:
        if line == "-1\n": break
        time, problem, result = line.split()
        time = int(time)
        if problem in problems:
            if result == "right":
                times[problem] = time
                problems[problem] = True
        else:
            times[problem] = time
            problems[problem] = result == "right"
    solved = 0
    time = 0
    for problem, solved_problem in problems.items():
        if solved_problem:
            time += times[problem]
            solved += 1
        else:
            time += 20
    print(solved, time)

if __name__ == "__main__":
    main()
