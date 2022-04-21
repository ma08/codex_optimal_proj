


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def modulo(num1, num2):
    return num1 % num2


def exponent(num1, num2):
    return num1 ** num2


def int_divide(num1, num2):
    return num1 // num2


def main():
    expression = input()
    expression = expression.split()
    num1 = int(expression[0])
    num2 = int(expression[2])
    operator = expression[1]
    if operator == '+':
        print(add(num1, num2))
    elif operator == '-':
        print(subtract(num1, num2))
    elif operator == '*':
        print(multiply(num1, num2))
    elif operator == '/':
        print(divide(num1, num2))
    elif operator == '%':
        print(modulo(num1, num2))
    elif operator == '**':
        print(exponent(num1, num2))
    elif operator == '//':
        print(int_divide(num1, num2))


if __name__ == "__main__":
    main()
