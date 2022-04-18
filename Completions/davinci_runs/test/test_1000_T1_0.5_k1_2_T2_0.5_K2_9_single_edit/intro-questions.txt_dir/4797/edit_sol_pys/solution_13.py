

def main():
    string = input()[::-1]
    stack = []
    for c in string:
        if c == '<':
            if stack:
                stack.pop()
        else:
            stack.append(c)
    print(''.join(stack)[::-1])

main()
