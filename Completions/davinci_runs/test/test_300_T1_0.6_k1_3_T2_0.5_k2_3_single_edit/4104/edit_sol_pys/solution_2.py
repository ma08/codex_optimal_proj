

def main():
    expression = input('Enter an expression: ')
    values = [float(x) for x in expression.split('-')]
    result = values[0]
    for value in values[1:]:
        result -= value
    print(result)

main()
