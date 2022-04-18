import sys

def main():
    string = sys.stdin.readline()
    stack = []
    for c in string:
        if c == '<':
            stack.pop()
        else:
            stack.append(c)
    print(''.join(stack))

main()
