

def brainfuck(expression):
    expression = expression.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
    expression = expression.split()
    result = []
    for i in range(len(expression)):
        if expression[i] == '*':
            result.append(int(expression[i-1]) * int(expression[i+1]))
        elif expression[i] == '/':
            result.append(int(expression[i-1]) // int(expression[i+1]))
        else:
            result.append(expression[i])
    result = ' '.join(result)
    result = result.replace('*', '').replace('/', '')
    return result

expression = input()
print(brainfuck(expression))
