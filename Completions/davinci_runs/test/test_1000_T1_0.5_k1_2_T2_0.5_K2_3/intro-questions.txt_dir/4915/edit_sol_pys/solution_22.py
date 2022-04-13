

def main():
    numberOfProblems = 0
    time = 0
    currentTime = 0
    currentProblem = ""
    problems = []
    times = []
    wrongs = []
    while True:
        line = input()
        if line == "-1":
            break
        line = line.split(" ")
        currentTime = int(line[0])
        currentProblem = line[1]
        if line[2] == "right":
            if currentProblem not in problems:
                numberOfProblems += 1
                time += currentTime
                problems.append(currentProblem)
                times.append(currentTime)
                wrongs.append(0)
        else:
            if currentProblem not in problems:
                problems.append(currentProblem)
                times.append(currentTime)
                wrongs.append(1)
            else:
                index = problems.index(currentProblem)
                wrongs[index] += 1

    for i in range(len(problems)):
        if wrongs[i] > 0:
            time += wrongs[i] * 20

    print(numberOfProblems, time)


if __name__ == "__main__":
    main()
