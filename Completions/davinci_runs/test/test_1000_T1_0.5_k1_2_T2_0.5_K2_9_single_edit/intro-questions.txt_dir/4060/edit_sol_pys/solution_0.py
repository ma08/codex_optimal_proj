import sys
sys.setrecursionlimit(10 ** 9)

def solution(n, s):
    if n == 0:
        return 1
    if n == 1:
        if s[0] == ')':
            return 0
        else:
            return 1
    if s[0] == ')':
        return 0
    else:
        return solution(n - 2, s[2:]) + solution(n - 1, s[1:])




n = int(input())
s = list(input())
print(solution(n, s))
