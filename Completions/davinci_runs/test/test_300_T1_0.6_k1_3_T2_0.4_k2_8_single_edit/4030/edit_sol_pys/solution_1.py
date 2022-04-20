

n = int(input())  # number of elements
s = input()  # input string


def solve(n, s):  # function to solve
    if n == 1:
        return 1
    if n == 2:
        return 1 if s[0] <= s[1] else 2

    start = 0  # start index
    cur = 0  # current index
    res = 0  # result
    for i in range(1, n):
        if s[i] < s[i - 1]:
            cur += 1
            res = max(res, cur)  # max of current and result
        else:
            cur = 0

    return res + 1


print(solve(n, s))
