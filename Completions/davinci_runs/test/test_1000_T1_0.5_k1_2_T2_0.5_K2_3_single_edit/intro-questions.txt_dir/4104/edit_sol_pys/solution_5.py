

def main():
    expression = input()
    expression = expression.split('+') #Разделяем на подстроки, разделитель "+"
    result = 0
    for i in expression:
        i = i.split('-') #Разделяем каждую подстроку, разделитель "-"
        for j in i:
            result += int(j)
        result -= len(i) - 1 #Вычитаем количество отрицательных чисел из результата
    print(result)

main()
