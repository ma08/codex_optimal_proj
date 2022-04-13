
import sys, collections

def main():
    times = collections.defaultdict(int)
    problems = collections.defaultdict(bool)
    while True:
        line = sys.stdin.readline()
        if line == "-1\n":
            break
        time, problem, result = line.split()
        time = int(time)
        if result == "right":
            times[problem] = time
            problems[problem] = True
        else: times[problem] += 20
    solved = 0
    time = 0
    for problem, solved_problem in problems.items():
        if solved_problem:
            time += times[problem]
            solved += 1
    print(solved, time)

if __name__ == "__main__":
    main()
