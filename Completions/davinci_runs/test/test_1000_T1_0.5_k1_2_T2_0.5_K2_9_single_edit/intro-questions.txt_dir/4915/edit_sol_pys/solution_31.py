

def main():
    while(True):
        n = int(input())
        if n == -1:
            break
        problems = [0] * n
        times = [0] * n
        wrongs = [0] * n
        for i in range(n):
            line = input()
            line = line.split(" ")
            currentTime = int(line[0])
            currentProblem = line[1]
            if line[2] == "right":
                if currentProblem not in problems:
                    problems[i] = 1
                    times[i] = currentTime
                    wrongs[i] = 0
            else:
                if currentProblem not in problems:
                    problems[i] = 1
                    times[i] = currentTime
                    wrongs[i] = 1
                else:
                    index = problems.index(currentProblem)
                    wrongs[index] += 1

        numberOfProblems = 0
        time = 0
        for i in range(len(problems)):
            if wrongs[i] > 0:
                time += wrongs[i] * 20
            else:
                time += times[i]
                numberOfProblems += 1

        print(numberOfProblems, time)

main()
