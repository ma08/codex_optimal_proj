

def main():
    k = int(input('Введите количество чисел Фибоначчи: '))
    a = 0
    b = 1
    for i in range(k):
        a, b = b, a + b
    print('Результат: ', a, b)

if __name__ == "__main__":
    main()
