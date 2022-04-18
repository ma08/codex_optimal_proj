
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
    num_solved = 0
    time = 0
    for problem, solved in problems.items():
        if solved:
            time += times[problem]
            num_solved += 1
        else:
            time += 20
    print(num_solved, time)

if __name__ == "__main__":
    main()
