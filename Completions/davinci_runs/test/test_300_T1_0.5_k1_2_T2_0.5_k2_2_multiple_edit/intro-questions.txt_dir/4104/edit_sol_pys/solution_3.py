
# Ввод выражения
def main():
    # Разделение по знаку +
    expression = input()
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

main()
