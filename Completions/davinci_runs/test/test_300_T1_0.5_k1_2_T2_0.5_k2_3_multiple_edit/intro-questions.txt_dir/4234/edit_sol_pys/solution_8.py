import sys

n = int(sys.stdin.readline())  # 입력받을 문자열의 길이
s = sys.stdin.readline().strip()  # 입력받을 문자열

stack = []
for i in range(n):
    stack.append(s[i])
    if len(stack) > 1 and stack[-1] == stack[-2]:
        stack.pop()
        stack.pop()

print(n - len(stack))
print(''.join(stack))
