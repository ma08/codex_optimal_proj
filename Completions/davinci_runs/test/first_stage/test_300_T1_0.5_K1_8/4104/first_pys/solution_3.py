

import sys

def main():
    # Read input
    expression = sys.stdin.readline().strip()

    # Split expression into operands
    operands = expression.split('+')

    # Remove all minus signs
    for i in range(len(operands)):
        operands[i] = operands[i].replace('-', '')

    # Convert operands to integers
    for i in range(len(operands)):
        operands[i] = int(operands[i])

    # Calculate result
    result = 0
    for i in range(len(operands)):
        result += operands[i]

    # Print result
    print(result)


if __name__ == '__main__':
    main()