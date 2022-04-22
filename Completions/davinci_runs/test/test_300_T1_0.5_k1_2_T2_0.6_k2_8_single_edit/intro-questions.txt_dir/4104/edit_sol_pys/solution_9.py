

def main():
    expression = input()
    expression = expression.split('-')
    result = 0
    for i in expression:
        i = i.split('+')
        for j in i:
            result += int(j)
        result -= len(expression) - 1
    print(result)

main()
