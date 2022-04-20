

n, k = map(int, input().split())
s = input()

def get_subsequences(s):
    return [s[:i] + s[i+1:] for i in range(len(s))]

def get_subsequences_recursive(s):
    if len(s) == 1:
        return [s]
    else:
        return get_subsequences_recursive(s[:-1]) + get_subsequences(s)

def get_subsequences_dp(s):
    dp = [[s[:i] + s[i+1:] for i in range(len(s))]]
    for _ in range(len(s) - 1):
        dp.append([])
        for i in range(len(dp[-2])):
            dp[-1] += get_subsequences(dp[-2][i])
    return [i for j in dp for i in j]

subsequences = get_subsequences_dp(s)

if len(subsequences) < k:
    print(-1)
else:
    print(sum(len(s) for s in subsequences[:k]))