

N = int(input())
S = input()

# 0:red, 1:blue

# stack
stack = []

for i in range(N):
    if len(stack) == 0:
        stack.append(S[i])
    else:
        if stack[-1] != S[i]:
            stack.pop()
        else:
            stack.append(S[i])

print(N - len(stack))