import sys

n = int(sys.stdin.readline())

stack = []
for i in range(n):
    command = sys.stdin.readline().strip()
    if command[:4] == 'push':
        stack.append(int(command.split()[1]))
    elif command == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif command == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)


import sys, collections

n = int(sys.stdin.readline().strip())
arr = collections.deque(sorted(list(map(int, sys.stdin.readline().strip().split()))))

if n == 1:
    print(0)
    print(arr[0])
    exit()

result = 0
while len(arr) > 1:
    result += arr[0] * arr[-1]
    arr.popleft()
    arr.pop()

if len(arr) == 1:
    result += arr[0]

print(result)
