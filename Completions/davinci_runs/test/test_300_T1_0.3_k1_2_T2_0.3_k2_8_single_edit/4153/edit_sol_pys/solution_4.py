

N = int(input())
S = input()

# stack
stack = [S[0]]

for i in range(N):
    if stack[-1] != S[i]:
        stack.pop()
    else:
        if stack[-1] != S[i]:
            stack.pop()
        else:
            stack.append(S[i])

print(N - len(stack))
