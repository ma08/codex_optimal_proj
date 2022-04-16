
import sys

n = int(input())
a = list(map(int, input().split()))

stack = []
for i in range(n):
    if len(stack) == 0 or a[i] > stack[-1]:
        stack.append(a[i])
        stack.reverse()
        for j in range(len(stack)):
            print(stack[j], end=' ')
        print()
    else:
        for j in range(len(stack)):
            if a[i] <= stack[j]:
                stack[j] = a[i]
                break
        stack.reverse()
        for j in range(len(stack)):
            print(stack[j], end=' ')
        print()
