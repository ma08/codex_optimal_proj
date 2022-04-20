

def brainfuck(expression):
    expression = expression.replace('+', ' + ').replace('-', ' - ').split()
    result = sum(int(x) for x in expression)
    return '+' * result + '>' + '<' * result + '[<+>-]<.'

expression = input()
print(brainfuck(expression))
