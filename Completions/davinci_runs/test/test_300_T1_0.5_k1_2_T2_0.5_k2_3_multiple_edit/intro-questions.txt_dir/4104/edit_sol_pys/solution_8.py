

def main():
    expression = input().split('+') # Разделяем выражение на числа, которые нужно сложить
    result = 0
    for i in expression:
        i = i.split('-') # Разделяем числа, которые нужно вычесть
        for j in i:
            result += int(j) # Складываем числа
        result -= len(i) - 1 # Вычитаем из результата количество чисел, которые нужно вычесть
    print(result)


main()
