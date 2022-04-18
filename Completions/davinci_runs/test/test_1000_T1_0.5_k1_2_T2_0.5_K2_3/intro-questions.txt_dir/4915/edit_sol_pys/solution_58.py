

def main():
    numberOfProblems = 0
    totalTime = 0.0
    currentTotalTime = 0
    currentProblem = ""
    problems = []
    totalTimes = []
    wrongs = []
    while True:
        line = input()
        if line == "-1":
            break
        line = line.split(" ")
        currentTotalTime = int(line[0])
        currentProblem = line[1]
        if line[2] == "right":
            if currentProblem not in problems:
                numberOfProblems += 1
                totalTime += float(currentTotalTime)
                problems.append(currentProblem)
                totalTimes.append(currentTotalTime)
                wrongs.append(0)
        else:
            if currentProblem not in problems:
                problems.append(currentProblem)
                totalTimes.append(currentTotalTime)
                wrongs.append(1)
            else:
                index = problems.index(currentProblem)
                wrongs[index] += 1

    for i in range(len(problems)):
        if wrongs[i] > 0:
            totalTime += wrongs[i] * 20.0

    print(numberOfProblems, totalTime)

main()
