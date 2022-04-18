

import sys
import math

    parameters = []
def main():
    input = sys.stdin.readline().strip()
    instructions = list(input)
    for i in range(len(instructions)):
        if instructions[i].isupper():
            parameters.append(instructions[i+1:i+1+math.ceil(ord(instructions[i])/4)].count('a'))
    print(math.ceil(max(parameters)/4))
 
if __name__ == '__main__':
    main()
