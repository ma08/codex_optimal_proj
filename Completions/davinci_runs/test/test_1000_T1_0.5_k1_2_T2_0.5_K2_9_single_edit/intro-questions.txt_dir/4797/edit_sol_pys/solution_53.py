

def main():
    string = input()
    stack = []
    for c in string:
        if c == '<':
            if stack:
                stack.pop()
        else:
            stack.append(c)
    print(''.join(stack))

main()
