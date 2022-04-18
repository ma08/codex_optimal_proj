

def solve(problems, k):
    i = 0
    problems = sorted(problems)
    for i in range(len(problems)):
        if k > problems[i]:
            k -= problems[i]
        else:
    print(i)
            break
    return i
