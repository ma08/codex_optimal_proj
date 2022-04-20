

def solve(problems, k):
    i = 0
    problems = list(reversed(problems))  # reverse problems list
    for i in range(len(problems)):
        if problems[i] > k:
            break
    return i
