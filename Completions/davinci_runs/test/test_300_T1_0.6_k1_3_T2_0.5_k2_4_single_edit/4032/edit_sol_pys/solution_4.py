

def solve(problems, k, d):
    i = 0
    problems.sort()
    problems.reverse()
    while i < len(problems):
        if problems[i] > k: break
        k -= problems[i]
        d -= 1
        if d == 0:
            i += 1
            d = 1
    return i
