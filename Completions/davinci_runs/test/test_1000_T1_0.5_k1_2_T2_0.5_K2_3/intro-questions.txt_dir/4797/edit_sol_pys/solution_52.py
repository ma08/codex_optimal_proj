#!/usr/bin/python3

def main():
    string = input()
    stack = []
    for i in string:
        if i == '<':
            stack.pop()
        else:
            stack.append(i)
    print(''.join(stack))

main()
