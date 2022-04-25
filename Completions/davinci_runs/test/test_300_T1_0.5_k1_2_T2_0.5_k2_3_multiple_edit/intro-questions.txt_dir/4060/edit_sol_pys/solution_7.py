import sys
sys.setrecursionlimit(10**6)



def solution(n, s)
    count = [[0, 0] for _ in range(n)]
    count[0][0] = 1 if s[0] == '(' else 0
    count[0][1] = 0 if s[0] == '(' else 1
    for i in range(1, n):
        if s[i] == '(':
            count[i][0] = count[i - 1][0] + 1
            count[i][1] = count[i - 1][1]
        else:
            count[i][0] = count[i - 1][0]
            count[i][1] = count[i - 1][1] + 1
    total = 0
    for i in range(n):
        if count[i][0] > count[i][1]:
            total += count[i][1]
        else:
            total += count[i][0]
    return total


def is_regular(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


n = int(input())
s = list(input())
print(solution(n, s))
