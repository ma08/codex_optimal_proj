

def main():
    expression = input()
    values = [int(x) for x in expression.split('/')]
    result = values[0]
    for value in values[1:]:
        result /= value
    print(result)

main()
