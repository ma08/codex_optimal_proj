

def solve(problems, k):
    i = 0
    problems = list(reversed(problems))
    for j in range(len(problems)):
        if problems[j] > k:
            break
    return j
