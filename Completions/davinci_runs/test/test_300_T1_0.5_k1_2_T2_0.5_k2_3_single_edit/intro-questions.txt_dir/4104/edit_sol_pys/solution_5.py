

def main():
    expression = input('Input expression: ')
    for i in range(len(expression)):
        expression[i] = expression[i].split('-')
    expression = expression.split('+')
    result = 0
    for i in expression:
        for j in range(len(i)):
            result += int(i[j])
        result -= len(i) - 1 
    print(result)

main()
