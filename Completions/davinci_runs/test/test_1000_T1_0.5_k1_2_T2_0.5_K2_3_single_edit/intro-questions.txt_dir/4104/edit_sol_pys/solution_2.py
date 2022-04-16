

def main():
    expression = input()
    expression = expression.split('+')  # разбиваем по +
    result = 0
    for i in expression:
        i = i.split('-')  # разбиваем по -
        for j in i:
            result += int(j)
        result -= len(i) - 1  # вычитаем отрицательные числа
    print(result)

main()
