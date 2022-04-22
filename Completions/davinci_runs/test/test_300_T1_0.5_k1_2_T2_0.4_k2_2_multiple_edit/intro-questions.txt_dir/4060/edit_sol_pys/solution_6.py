

def solution(n, p, q):
    count = 0
    for i in range(n):
        if q[i] == ')':
            if i > 0:
                q[i - 1] = '(' if q[i - 1] == ')' else ')'
                if is_regular(q):
                    count += 1
                q[i - 1] = '(' if q[i - 1] == ')' else ')'
        else:
            if i < n - 1:
                q[i + 1] = '(' if q[i + 1] == ')' else ')'
                if is_regular(q):
                    count += 1
                q[i + 1] = '(' if q[i + 1] == ')' else ')'
    return count


def is_regular(q):
    stack = []
    for c in q:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


n = int(input())
p = list(input())
q = list(input())
print(solution(n, p, q))
