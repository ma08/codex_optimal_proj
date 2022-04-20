
import sys
import re

def bf(n):
    if n == 0:
        return ''
    if n > 0:
        return '+' + bf(n-1)
    return '-' + bf(n+1)

def calculator(string):
    """returns the brainfuck program"""
    string = re.sub('\s', '', string)
    numbers = [int(n) for n in re.findall('\d+', string)]
    signs = re.findall('[+-]', string)
    result = numbers[0]
    program = ''
    for i in range(len(numbers[1:])):
        program += bf(numbers[i+1] - result)
        result += numbers[i+1]
        program += '>'
    program += bf(numbers[-1] - result)
    result += numbers[-1]
    program += '>'
    program += bf(-result)
    program += '<>'
    program += '[<'
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
    program += '.'
    return program

if __name__ == '__main__':
    print(calculator(sys.stdin.read()))
