

def solution(n, a):
    count = 0
    for i in range(n):
        if a[i] == ')':
            if i > 0:
                a[i - 1] = '(' if a[i - 1] == ')' else ')'
                if is_regular(a):
                    count += 1
                a[i - 1] = '(' if a[i - 1] == ')' else ')'
        else:
            if i < n - 1:
                a[i + 1] = '(' if a[i + 1] == ')' else ')'
                if is_regular(a):
                    count += 1
                a[i + 1] = '(' if a[i + 1] == ')' else ')'
    return count


def is_regular(a):
    stack = []
    for i in range(len(a)):
        if a[i] == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


n = int(input())
s = list(input())
print(solution(n, s))
