

def main():
    string = input("Enter the string: ")
    stack = []
    for c in string:
        if c == '<':
            stack.pop()
        else:
            stack.append(c)
    print("".join(stack))

main()
