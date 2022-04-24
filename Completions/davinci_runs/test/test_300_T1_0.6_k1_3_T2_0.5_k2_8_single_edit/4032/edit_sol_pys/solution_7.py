

def solve(problems, k, l):
    i = 0
    problems = list(reversed(problems))
    for i in range(len(problems)):
        if problems[i] > k:
            break
    return i
