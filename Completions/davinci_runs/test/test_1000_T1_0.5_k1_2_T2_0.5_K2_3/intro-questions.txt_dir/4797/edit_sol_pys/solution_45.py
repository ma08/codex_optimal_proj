

def main():
    string = input().strip()
    stack = []
    for i in string:
        if i == '<':
            if stack:
                stack.pop()
        else:
            stack.append(i)
    print(''.join(stack))

main()
