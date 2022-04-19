import sys
import collections

sys.setrecursionlimit(10**6)


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



def solution(n, s):
    count = 0
    for i in range(n):
        if s[i] == ')':
            if i > 0:
                s[i - 1] = '(' if s[i - 1] == ')' else ')'
                if is_regular(s):
                    count += 1
                s[i - 1] = '(' if s[i - 1] == ')' else ')'
        else:
            if i < n - 1:
                s[i + 1] = '(' if s[i + 1] == ')' else ')'
                if is_regular(s):
                    count += 1
                s[i + 1] = '(' if s[i + 1] == ')' else ')'
    return count



def solution_recursive(n, s):
    count = 0
    for i in range(n):
        if s[i] == ')':
            if i > 0:
                s[i - 1] = '(' if s[i - 1] == ')' else ')'
                count += solution_recursive(n, s)
                s[i - 1] = '(' if s[i - 1] == ')' else ')'
        else:
            if i < n - 1:
                s[i + 1] = '(' if s[i + 1] == ')' else ')'
                count += solution_recursive(n, s)
                s[i + 1] = '(' if s[i + 1] == ')' else ')'
    return count


def solution_recursive_memo(n, s, memo):
    if not is_regular(s):
        return 0
    if s in memo:
        return memo[s]
    count = 0
    for i in range(n):
        if s[i] == ')':
            if i > 0:
                s[i - 1] = '(' if s[i - 1] == ')' else ')'
                count += solution_recursive_memo(n, s, memo)
                s[i - 1] = '(' if s[i - 1] == ')' else ')'
        else:
            if i < n - 1:
                s[i + 1] = '(' if s[i + 1] == ')' else ')'
                count += solution_recursive_memo(n, s, memo)
                s[i + 1] = '(' if s[i + 1] == ')' else ')'
    memo[s] = count
    return count


def solution_recursive_memo_dp(n, s, memo):
    if not is_regular(s):
        return 0
    if s in memo:
        return memo[s]
    count = 0
    for i in range(n):
        if s[i] == ')':
            if i > 0:
                s[i - 1] = '(' if s[i - 1] == ')' else ')'
                count += solution_recursive_memo_dp(n, s, memo)
                s[i - 1] = '(' if s[i - 1] == ')' else ')'
        else:
            if i < n - 1:
                s[i + 1] = '(' if s[i + 1] == ')' else ')'
                count += solution_recursive_memo_dp(n, s, memo)
                s[i + 1] = '(' if s[i + 1] == ')' else ')'
    memo[s] = count
    return count


def solution_recursive_memo_dp_reverse(n, s, memo):
    if not is_regular(s):
        return 0
    if s in memo:
        return memo[s]
    count = 0
    for i in range(n - 1, -1, -1):
        if s[i] == '(':
            if i < n - 1:
                s[i + 1] = '(' if s[i + 1] == ')' else ')'
                count += solution_recursive_memo_dp_reverse(n, s, memo)
                s[i + 1] = '(' if s[i + 1] == ')' else ')'
        else:
            if i > 0:
                s[i - 1] = '(' if s[i - 1] == ')' else ')'
                count += solution_recursive_memo_dp_reverse(n, s, memo)
                s[i - 1] = '(' if s[i - 1] == ')' else ')'
    memo[s] = count
    return count


n = int(input())
s = list(input())
print(solution(n, s))
