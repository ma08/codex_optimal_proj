

def brainfuck(expression):
    expression = expression.replace('+', ' + ').replace('-', ' - ').replace(' ', '')
    expression = expression.split()
    result = 0
    for i in range(0, len(expression), 2):
        if expression[i+1] == '+':
            result += int(expression[i])
        elif expression[i+1] == '-':
            result -= int(expression[i])
    result = result % 256
    # print(result)
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
