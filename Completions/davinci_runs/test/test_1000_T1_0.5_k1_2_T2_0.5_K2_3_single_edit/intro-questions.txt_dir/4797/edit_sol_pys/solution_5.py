

def main():
    string = raw_input()
    stack = []
    for c in string:
        if c == '<':
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(c)
    print(''.join(stack))

main()
