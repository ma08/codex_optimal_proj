

def solution(n, s):
    count = 0
    for i in range(n):
        if s[i] == ')':
            if i > 0:
                s[i - 1] = '(' if s[i - 1] == ')' else ')'
                if is_regular(s):
                    count += 1
                s[i - 1] = ')' if s[i - 1] == '(' else '('
        else:
            if i < n - 1:
                s[i + 1] = '(' if s[i + 1] == ')' else ')'
                if is_regular(s):
                    count += 1
                s[i + 1] = ')' if s[i + 1] == '(' else '('
    return count


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
