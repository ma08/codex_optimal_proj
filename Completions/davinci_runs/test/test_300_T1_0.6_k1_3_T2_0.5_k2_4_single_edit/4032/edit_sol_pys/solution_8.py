

def solve(problems, k, n):
    i = 0
    problems = list(reversed(problems))
    for i in range(n):
        if problems[i] > k:
            break
    return i
