

def solve(problems, k):
    problems = list(reversed(problems))
    for i in range(len(problems)):
        if problems[i] > k:
            break
    return i
