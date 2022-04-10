

def main():
    string = input()
    stack = []
    for c in string:
        if c == '<':
            stack.pop()
        else:
            stack.append(c)
    print(''.join(stack))

main()