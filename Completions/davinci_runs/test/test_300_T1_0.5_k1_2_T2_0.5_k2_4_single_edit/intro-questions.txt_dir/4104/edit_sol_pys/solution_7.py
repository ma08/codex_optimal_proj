

def main():
    expression = input()
    expression = expression.split('+')
    result = 0
    for i in expression:
        i = i.split('-')
        result += int(i[0])
        result -= len(i) - 2
    print(result)

main()
