
#!/usr/bin/python3

def plus(n1, n2):
    return n1 + n2


def minus(n1, n2):
    return n1 - n2


def calc(operators, operands):
    result = operands[0]
    for i in range(len(operands) - 1):
        result = operators[i](result, operands[i + 1])
    return result


def main():
    try:
        while True:
            operators = []
            operands = []
            expression = input().split()
            for item in expression:
                if item == "+":
                    operators.append(plus)
                elif item == "-":
                    operators.append(minus)
                else:
                    operands.append(int(item))
            print(calc(operators, operands))
    except EOFError:
        pass


if __name__ == "__main__":
    main()
