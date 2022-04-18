def main():
    expression = input()
    expression = expression.split('+')[1:]
    result = 0
    for i in expression:
        i = i.split('-')[1:]
        for j in i:
            result += int(j)
        result -= len(i)
    print(result)

main()
