n = int(input())
a = [int(i) for i in input().split()]

def print_stack(stack):
    for i in range(len(stack)):
        print(stack[i], end=' ')
    print()

stack = []
for i in range(n):
    stack.append(a[i])
    print_stack(stack[::-1])
