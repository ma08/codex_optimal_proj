
# Ввод выражения
    expression = input()
def main():
    # Разделение по знаку +
    # Результат выполнения выражения
    expression = expression.split('+')
    # Проход по всем числам, отделенным знаком +
    result = 0
    for i in expression:
        i = i.split('-')
        for j in i:
            result += int(j)
        result -= len(i) - 1
    print(result)

if __name__ == '__main__':
    main()
