

def calc(expression):
    result = 0
    for i in expression:
        i = i.split('-')
        for j in i:
            result += int(j)
        result -= len(i) - 1
    return result

def main():
    expression = input()
    expression = expression.split('+')
    print(calc(expression))

main()
