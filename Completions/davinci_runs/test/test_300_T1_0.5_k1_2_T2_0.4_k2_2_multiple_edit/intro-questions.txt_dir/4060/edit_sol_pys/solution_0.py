
def solution(n, p):
    count = 0
    for i in range(n):
        if p[i] == ')':
            if i > 0:
                p[i - 1] = '(' if p[i - 1] == ')' else ')'
                if is_regular(p):
                    count += 1
                p[i - 1] = '(' if p[i - 1] == ')' else ')'
        else:
            if i < n - 1:
                p[i + 1] = '(' if p[i + 1] == ')' else ')'
                if is_regular(p):
                    count += 1
                p[i + 1] = '(' if p[i + 1] == ')' else ')'
    return count


def is_regular(p):
    stack = []
    for c in p:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


n = int(input())
p = list(input())
print(solution(n, p))
