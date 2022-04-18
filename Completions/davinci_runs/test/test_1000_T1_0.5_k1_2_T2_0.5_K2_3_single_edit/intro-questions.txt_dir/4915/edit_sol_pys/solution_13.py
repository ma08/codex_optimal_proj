

import sys

def main():
    times = dict()
    problems = dict()
    while True:
        line = sys.stdin.readline()
        if line == "-1\n":
            break
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
    for problem, solved in problems.items():
        if solved:
            time += times[problem]
            solved += 1
        elif problems[problem] == False:
            time += 20
    print(solved, time)

if __name__ == "__main__":
    main()
