

def solve(problems, k):
    i = 0
    problems = list(reversed(problems))
    for i in range(len(problems)):
        if problems[i] > k:
            break


print(solve([1, 2, 3], 2))
    return i
