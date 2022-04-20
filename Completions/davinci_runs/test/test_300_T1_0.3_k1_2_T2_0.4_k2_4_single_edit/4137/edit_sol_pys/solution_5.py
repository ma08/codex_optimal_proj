

def brainfuck(expression):
    expression = expression.replace('+', ' + ').replace('-', ' - ').replace(' ', '')
    expression = expression.split()
    result = 0
    for i in range(len(expression)):
        if expression[i] == '+': result += 1
        elif expression[i] == '-': result -= 1
    result = result % 256 + 256
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
