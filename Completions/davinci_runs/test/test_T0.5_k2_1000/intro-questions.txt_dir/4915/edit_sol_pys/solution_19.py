
import sys

def main():
    times = dict()
    problems = dict()
    while True:
        line = sys.stdin.readline()
        if line == "-1\n":
            break
        time, problem, result = line.split()[:3]
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
    for problem, correct in problems.items():
        if correct:
            time += times[problem]
            solved += 1
        else:
            time += 20 * (times[problem] // 20 + 1)
    print(solved, time)

if __name__ == "__main__":
    main()
