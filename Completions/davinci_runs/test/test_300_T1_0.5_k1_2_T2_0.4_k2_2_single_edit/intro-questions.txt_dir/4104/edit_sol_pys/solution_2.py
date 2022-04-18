

def main():
    expression = input()
    expression = expression.split('+')
    result = 0
    for i in expression:
        result -= len(i) - 1
        i = i.split('-')
        for j in i:
            result += int(j)
    print(result)

main()
