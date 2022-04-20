

import sys

def main():
    # Read input
    s = sys.stdin.readline()

    # Solve
    result = solve(s)

    # Print result
    print(result)

def solve(s):
    """
    """
    # Initialize
    stack = []
    result = ''

    # Parse string
    for char in s:
        if char == '?':
            pass
        elif char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return 'false'
            else:
                stack.pop()
        elif char == '_':
            result += '0'
        elif char == '-':
            result += '1'
        elif char == '+':
            result += '2'
        elif char == '/':
            result += '3'
        elif char == '*':
            result += '4'
        elif char == ':':
            pass
        elif char == '>':
            pass
        elif char == ',':
            pass
        elif char == '<':
            pass
        elif char == '.':
            pass

    # Check if stack is empty
    if len(stack) != 0:
        return 'false'

    return result

if __name__ == '__main__':
    main()