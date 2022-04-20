
def main():
    num = int(input())  # число элементов в массиве
    for i in input().split():  # проверяем числа на условие
        if int(i) % 2 == 0 and int(i) % 3 != 0 and int(i) % 5 != 0:  # если число не делится на 2 и на 3 и на 5
            print("DENIED")  # то выводим DENIED
            exit()  # и выходим из цикла
    print("APPROVED")  # если все числа делятся на 2 или на 3 или на 5, то выводим APPROVED

if __name__ == '__main__':
    main()
