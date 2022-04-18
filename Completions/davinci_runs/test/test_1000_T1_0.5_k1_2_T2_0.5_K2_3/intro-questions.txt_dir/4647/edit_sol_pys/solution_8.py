

from sys import stdin
from collections import deque

input_lines = deque(stdin.read().splitlines())

# Read the number of lines
n = int(input_lines.popleft()) 

# Read the lines
lines = [input_lines.popleft() for _ in range(n)]

# Initialize the result
result = ''

for line in lines:
    # Initialize the stack
    stack = []

    # Iterate over the line
    for c in line:
        # If the character is a closing bracket
        if c in ')]}':
            # Get the last character from the stack
            last = stack.pop()

            # If the character is not a matching opening bracket
            if not (c == ')' and last == '(' or c == ']' and last == '[' or c == '}' and last == '{'):
                # Add the character to the stack
                stack.append(last)
                stack.append(c)

                # Stop iterating over the line
                break

        # If the character is an opening bracket
        elif c in '({[':
            # Add the character to the stack
            stack.append(c)

    # If the stack is empty
    if len(stack) == 0:
        # Add the line to the result
        result += line + '\n'

# Print the result to standard output
print(result)
