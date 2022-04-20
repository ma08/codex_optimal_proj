#!/usr/bin/env python3

import sys

def main():
    line = sys.stdin.read().strip()
    operands = line.split('+')
    result = 0
    for operand in operands:
        operand = operand.split('-')
        result += int(operand[0])
        for i in range(1, len(operand)):
            result -= int(operand[i])
    print(result)

if __name__ == '__main__':
    main()
