

n, k = map(int, input().split())
problems = list(map(int, input().split()))

def solve(problems, k):
    if not problems:
        return 0
    if problems[0] <= k:
        return 1 + solve(problems[1:], k)
    elif problems[-1] <= k:
        return 1 + solve(problems[:-1], k)
    else:
        return 0

print(solve(problems, k))