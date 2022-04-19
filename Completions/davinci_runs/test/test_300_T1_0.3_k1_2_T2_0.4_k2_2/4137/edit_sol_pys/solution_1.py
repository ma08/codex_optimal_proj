

def brainfuck(expression):
    expression = expression.replace('+', ' + ').replace('-', ' - ').replace(' ', '')
    expression = expression.split()
    result = 0
    for i in range(0, len(expression), 2):
        if i+1 < len(expression):
            if expression[i] == '+':
                result += int(expression[i+1])
            else:
                result -= int(expression[i+1])
        result = result % 256
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
