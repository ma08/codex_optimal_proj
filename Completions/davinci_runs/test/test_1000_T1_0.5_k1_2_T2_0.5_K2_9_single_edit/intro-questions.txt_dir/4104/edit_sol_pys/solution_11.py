

def main():
    expression = input()
    expression = expression.split('+')  # разбиваем выражение на части
    result = 0
    for i in expression:  # проходим по каждой части выражения
        i = i.split('-')  # разбиваем часть на подчасти
        for j in i:  # проходим по каждой подчасти
            result += int(j)  # прибавляем к результату
        result -= len(i) - 1  # вычитаем количество подчастей минус один
    print(result)

main()
