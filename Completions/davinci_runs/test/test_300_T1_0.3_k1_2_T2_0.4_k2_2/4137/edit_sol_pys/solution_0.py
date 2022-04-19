

def brainfuck(expression):
    expression = expression.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
    expression = expression.split()
    result = 0
    if len(expression) == 1:
        result = int(expression[0])
    else:
        result = int(expression[0])
        for i in range(1, len(expression), 2):
            if expression[i] == '+':
                result += int(expression[i+1])
            elif expression[i] == '-':
                result -= int(expression[i+1])
            elif expression[i] == '*':
                result *= int(expression[i+1])
            else:
                result //= int(expression[i+1])
    result = abs(result) % 256
    bf = ''
    for i in range(result):
        bf += '+'
    bf += '>'
    for i in range(result):
        bf += '<'
    bf += '[<+>-]<'
    bf += '.'
    return bf

expression = input()
print(brainfuck(expression))
