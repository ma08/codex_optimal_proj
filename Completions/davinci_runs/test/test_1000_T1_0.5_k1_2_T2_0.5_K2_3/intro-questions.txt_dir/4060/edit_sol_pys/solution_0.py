def solution(n, s):
    if n % 2 == 1:
        return 0


    stack = []
    count = 0
    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return 0
            if i - stack[-1] == 1:
                stack.pop()
            else:
                count += 1
                stack.pop()
    return count


n = int(input())
s = list(input())
print(solution(n, s))
