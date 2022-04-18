

def main():
    numberOfProblems = 0
    time = 0
    current_time = 0
    currentProblem = ""
    problems = []
    times = []
    wrongs = []
        print("Enter:")
    while True:
        line = input()
        if line == "":
            break
        line = line.split(" ")
        current_time = int(line[0])
        currentProblem = line[1]
        if line[2] == "right":
            if currentProblem not in problems:
                numberOfProblems += 1
                time += current_time
                problems.append(currentProblem)
                times.append(current_time)
                wrongs.append(0)
        else:
            if currentProblem not in problems:
                problems.append(currentProblem)
                times.append(current_time)
                wrongs.append(1)
            else:
                index = problems.index(currentProblem)
                wrongs[index] += 1

    for i in range(len(problems)):
        if wrongs[i] > 0:
            time += wrongs[i] * 20

    print(numberOfProblems, time)

main()
