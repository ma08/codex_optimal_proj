

def main():
    expression = input()
    expression = expression.split('+')
    result = 0
    for num in expression:
        num = num.split('-')
        for j in num:
            result += int(num)
        result -= len(num) - 1
    print(result)

main()
