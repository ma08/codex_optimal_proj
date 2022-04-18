

def solve(problems, k):
    i = 0
    problems = list(reversed(problems))
    for i in range(len(problems)-1):
        if problems[i] > k:
            break
    return i+1
