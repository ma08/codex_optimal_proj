

n = int(input())
a = [int(x) for x in input().split()]

stack = []

ans = []

for i in range(n):
    if len(stack) == 0:
        stack.append(a[i])
        ans.append('L')
    elif stack[-1] < a[i]:
        stack.append(a[i])
        ans.append('L')
    else:
        while len(stack) > 0 and stack[-1] > a[i]:
            stack.pop()
        if len(stack) == 0:
            stack.append(a[i])
            ans.append('L')
        elif stack[-1] < a[i]:
            stack.append(a[i])
            ans.append('L')
        else:
            stack.pop()
            ans.append('R')

print(len(stack))
print(''.join(ans))