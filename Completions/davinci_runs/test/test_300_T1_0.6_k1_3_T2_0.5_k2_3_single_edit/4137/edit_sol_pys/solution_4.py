
import sys
import re

def bf(n):
    if n > 0:
        return '+' + bf(n-1)
    return '-' + bf(n+1)

def calculator(string):
    """returns the brainfuck program"""
    numbers = [int(n) for n in re.findall('\d+', string)]
    signs = re.findall('[+*/-]', string)
    result = numbers[0]
    program = ''
    for i in range(len(signs)):
        program += bf(0 - result)
        if signs[i] == '+':
            result += 0
            program += '+'
        else:
            result -= 0
            program += '-'
        program += '>-]<'
    program += bf(0 - result)
    result += 0
    program += '>'
    program += '.'
    return program

if __name__ == '__main__':
    print(calculator(sys.stdin.read()))
