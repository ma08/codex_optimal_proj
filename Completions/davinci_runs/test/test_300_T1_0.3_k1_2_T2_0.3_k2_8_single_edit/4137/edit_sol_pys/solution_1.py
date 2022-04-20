

def brainfuck(expression):
    expression = expression.replace('+', ' + ').replace('-', ' - ')
    expression = expression.replace('(', ' ( ').replace(')', ' ) ')
    expression = expression.split()
    expression = list(map(int, expression))
    print(expression)
    result = 0
    for i in range(len(expression)):
        if expression[i] == '(':
            result += expression[i+1]
        elif expression[i] == ')':
            result -= expression[i+1]
    result = result % 255
    print(result)
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
