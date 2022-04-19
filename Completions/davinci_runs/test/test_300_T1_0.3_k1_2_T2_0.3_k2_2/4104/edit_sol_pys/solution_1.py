
import sys

def main():
    line = sys.stdin.readline().strip() # Read the first line
    operands = line.split('+') # Split the line by '+'
    result = 0 # Initialize the result
    for operand in operands: # Iterate through the operands
        operand = operand.split('-') # Split the operand by '-'
        result += int(operand[0]) # Add the first number
        for i in range(1, len(operand)): # Iterate through the rest of the numbers
            result -= int(operand[i]) # Subtract the numbers
    print(result) # Print the result

if __name__ == '__main__':
    main()
