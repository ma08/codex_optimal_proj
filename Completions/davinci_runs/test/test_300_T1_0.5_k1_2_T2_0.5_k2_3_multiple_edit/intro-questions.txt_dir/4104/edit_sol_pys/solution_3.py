def main():
    # expression = '1+2-3+4-5-6+7'
    expression = input()
    expression = expression.split('+')
    # print(expression)
    result = 0
        # print(i)
    for i in expression:
        # print(i)
        i = i.split('-')
            # print(j)
        for j in i:
            # print(result)
            result += int(j)
        result -= len(i) - 1
    print(result)

main()
