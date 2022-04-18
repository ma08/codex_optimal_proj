def main():
    with open('input.txt', 'r') as f:
        expression = f.readline()
        expression = expression.split('+')
        result = 0
        for i in expression:
            i = i.split('-')
            for j in i:
                result += int(j)
            result -= len(i) - 1
        print(result)

main()
