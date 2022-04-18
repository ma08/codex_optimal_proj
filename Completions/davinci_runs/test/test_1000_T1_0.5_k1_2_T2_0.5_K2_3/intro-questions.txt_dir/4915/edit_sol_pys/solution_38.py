

def main():
    numberOfProblems = 0
    totalTime = 0
    currentProblem = ""
    problems = []
    totalTimes = []
    wrongs = []
    while True:
        line = input()
        if line == "-1":
            break
        line = line.split(" ")
        currentTotalTime = int(line[0]) + (int(line[3]) * 20)
        currentProblem = line[1]
        if line[2] == "right":
            if currentProblem not in problems:
                numberOfProblems += 1
                totalTime += currentTotalTime
                problems.append(currentProblem)
        else:
            if currentProblem not in problems:
                problems.append(currentProblem)
            else:
                index = problems.index(currentProblem)
                totalTime += currentTotalTime

    print(numberOfProblems, totalTime)

main()
