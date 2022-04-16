

def main():
    number_of_problems = 0
    time = 0
    current_time = 0
    current_problem = ""
    problems = []
    times = []
    wrongs = []
    while True:
        line = input()
        if line == "-1":
            break
        line = line.split(" ")
        current_time = int(line[0])
        current_problem = line[1]
        if line[2] == "right":
            if current_problem not in problems:
                number_of_problems += 1
                time += current_time
                problems.append(current_problem)
                times.append(current_time)
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

main()
