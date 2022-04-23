

def solution(n, s):  # n: 문자열의 길이, s: 문자열
    count = 0
    for i in range(n):
        if s[i] == ')':
            if i > 0:
                s[i - 1] = '(' if s[i - 1] == ')' else ')'
                if is_regular(s):  # 일치시키기 전과 후의 문자열이 일치하는지 확인
                    count += 1
                s[i - 1] = ')' if s[i - 1] == '(' else '('
        else:
            if i < n - 1:
                s[i + 1] = '(' if s[i + 1] == ')' else ')'
                if is_regular(s):
                    count += 1
                s[i + 1] = ')' if s[i + 1] == '(' else '('
    return count


def is_regular(s):  # 일치하는지 확인하는 함수
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
