
import sys

def main():
    times = {}
    problems = {}
    while True:
        line = sys.stdin.readline()
        if line == "-1":
            break
        time, problem, result = line.split(" ")
        time = int(time)
        if result == "right":
            times[problem] = time
            problems[problem] = True
        elif problem not in problems:
            problems[problem] = False
    solved = 0
    time = 0
    for problem, solved_problem in problems.items():
        if solved_problem:
            time += times[problem]
            solved += 1
        else:
            time += 20 * (times[problem] // 20 + 1)
    print(solved, time)

if __name__ == "__main__":
    main()
