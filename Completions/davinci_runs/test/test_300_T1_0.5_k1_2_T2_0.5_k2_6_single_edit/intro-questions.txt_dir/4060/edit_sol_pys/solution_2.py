

def solution(n, parentheses):
    answer = 0
    for i in range(n-1):
        for j in range(i+1, n):
            temp = parentheses[i:j+1]
            if is_regular(temp):
                answer += 1
    return answer



def is_regular(parentheses):
    stack = []
    for p in parentheses:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack


n = int(input())
parentheses = input()
print(solution(n, parentheses))
