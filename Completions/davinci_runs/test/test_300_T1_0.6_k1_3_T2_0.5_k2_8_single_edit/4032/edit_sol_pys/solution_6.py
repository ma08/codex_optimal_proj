

def solve(problems, k):
    i = 0
    problems = problems[::-1]
    for i in range(len(problems)):
        if problems[i] > k:
            break
    return i
