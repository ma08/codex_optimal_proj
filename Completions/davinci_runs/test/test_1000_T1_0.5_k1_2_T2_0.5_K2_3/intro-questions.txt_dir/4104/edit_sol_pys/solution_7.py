

def main(expression):
    expression = expression.split('+')
    result = []
    for i in range(len(expression)):
        if '-' in expression[i]:
            expression[i] = expression[i].split('-')
            for j in range(len(expression[i])):
                if j == 0:
                    result.append(int(expression[i][j]))
                else:
                    result.append(-int(expression[i][j]))
        else:
            result.append(int(expression[i]))
    return sum(result)


expression = input()
print(main(expression))
