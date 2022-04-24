

def solve(problems, k):
    i = 0
    problems = list(reversed(sorted(problems)))
    for i in range(len(problems)-1):
        if problems[i] > k:
            break
    return i
