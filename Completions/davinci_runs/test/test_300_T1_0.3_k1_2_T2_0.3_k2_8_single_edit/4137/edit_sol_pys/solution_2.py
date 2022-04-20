

def brainfuck(expression):
    expression = expression.replace('+', ' + ').replace('-', ' - ')
    expression = expression.split()
    result = int(expression[0])
    for i in range(1, len(expression), 2):
        if expression[i] == '+':
            result += int(expression[i+1])
        else:
            result -= int(expression[i+1])
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
