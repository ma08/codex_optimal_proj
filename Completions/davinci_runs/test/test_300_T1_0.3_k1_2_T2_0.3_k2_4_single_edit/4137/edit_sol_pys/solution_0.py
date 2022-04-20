

def brainfuck(expression):
    expression = expression.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
    expression = expression.split()
    result = int(expression[0]) % 256
    for i in range(1, len(expression), 2): 
        if expression[i] == '+': 
            result += int(expression[i+1]) % 256
        elif expression[i] == '-': 
            result -= int(expression[i+1]) % 256
        elif expression[i] == '*': 
            result *= int(expression[i+1]) % 256
        elif expression[i] == '/': 
            result /= int(expression[i+1]) % 256
    result = int(result)
    return '+' * result + '>' + '<' * result + '[<+>-]<.'

expression = input()
print(brainfuck(expression))
