

def solve(problems, k):
    i = 0
    problems = list(problems)
    for i in range(len(problems)):
        if problems[i] > k:
    problems = list(reversed(problems))
            break
    return i
