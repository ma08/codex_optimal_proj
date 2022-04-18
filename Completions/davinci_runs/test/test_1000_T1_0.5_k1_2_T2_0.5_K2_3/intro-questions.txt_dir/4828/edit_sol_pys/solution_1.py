

import sys
import math

def main():
    input = sys.stdin.readline().strip()
    instructions = list(input)
    parameters = []
    for i in range(len(instructions)):
        if instructions[i].isupper():
            parameters.append(instructions[i+1:i+1+math.ceil(ord(instructions[i])/4)].count('a'))  # a = 1, b = 2, c = 3, d = 4
    print(math.ceil(max(parameters)/4))

if __name__ == '__main__':
    main()
