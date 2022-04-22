

def main():
    expression = input()
    expression = expression.split('+')  # строка превращается в список по плюсам
    result = 0
    for i in expression:
        i = i.split('-')  # список превращается в список списков по минусам
        for j in i:
            result += int(j)  # каждое число прибавляется к результату
        result -= len(i) - 1  # вычитается количество минусов в подсписке
    print(result)

main()
