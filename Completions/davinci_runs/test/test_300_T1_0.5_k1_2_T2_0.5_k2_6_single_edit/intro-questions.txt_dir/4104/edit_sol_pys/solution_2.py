

def main():
    expression = input()
    expression = expression.split('+') # Разбиваем на слагаемые
    result = 0
    for i in expression:
        i = i.split('-') # Разбиваем на части
        for j in i:
            result += int(j) # Прибавляем к результату
        result -= len(i) - 1 # Вычитаем количество частей минус 1
    print(result)

main()
